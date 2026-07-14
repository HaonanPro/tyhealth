"""Deploy optimized images + updated HTML/CSS/JS to server"""
import paramiko
import os
import sys

HOST = '43.134.18.109'
USER = 'ubuntu'
PASS = 'haonan2026!'
REMOTE_ROOT = '/var/www/mysite'
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("Deploy optimized site (WebP images + updated HTML)")
print("=" * 60)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)

sftp = ssh.open_sftp()

# Files to upload
files = [
    'index.html',
    'styles.css',
    'script.js',
]

# WebP images to upload
webp_images = [
    'AKK.webp',
    'page_06.webp',
    'page_30.webp',
    'page_31.webp',
    'p04_03.webp',
    'p31_03.webp',
    'p30_04.webp',
    'expert-zhangyousheng.webp',
    'expert-liusuchun.webp',
    'hero-wujitai.webp',
    'hero-tengcha-product.webp',
    'hero-slide-p04.webp',
    'hero-slide-p31.webp',
    'p13_01.webp',
    'p30_03.webp',
]

uploaded = 0
errors = 0

# Upload core files
for f in files:
    local_path = os.path.join(LOCAL_DIR, f)
    remote_path = f'{REMOTE_ROOT}/{f}'
    try:
        sftp.put(local_path, f'/tmp/{f}')
        ssh.exec_command(f'sudo mv /tmp/{f} {remote_path}')
        print(f'[OK] {f}')
        uploaded += 1
    except Exception as e:
        print(f'[ERR] {f}: {e}')
        errors += 1

# Upload WebP images - need sudo for assets dir
for img in webp_images:
    local_path = os.path.join(LOCAL_DIR, 'assets', img)
    if not os.path.exists(local_path):
        print(f'[SKIP] {img} (not found locally)')
        continue
    remote_path = f'{REMOTE_ROOT}/assets/{img}'
    try:
        # Upload to /tmp first, then sudo mv
        sftp.put(local_path, f'/tmp/{img}')
        stdin, stdout, stderr = ssh.exec_command(f'sudo mv /tmp/{img} {remote_path}')
        stdout.channel.recv_exit_status()
        print(f'[OK] assets/{img}')
        uploaded += 1
    except Exception as e:
        print(f'[ERR] assets/{img}: {e}')
        errors += 1

# Update Nginx cache rules to include .webp
nginx_update = r"""
sudo sed -i 's/\\\\.(jpg|jpeg|png|gif|ico|svg|woff|woff2)$/\\\\.(jpg|jpeg|png|gif|ico|svg|woff|woff2|webp)$/' /etc/nginx/conf.d/tyhealthtech.conf
sudo sed -i 's/\\\\.(jpg|jpeg|png|gif|ico|svg|woff|woff2)$/\\\\.(jpg|jpeg|png|gif|ico|svg|woff|woff2|webp)$/' /etc/nginx/sites-enabled/mysite
"""
stdin, stdout, stderr = ssh.exec_command(nginx_update)
stdout.channel.recv_exit_status()

# Add gzip for text assets
gzip_config = """
# Check if gzip is already enabled
if ! grep -q 'gzip on' /etc/nginx/nginx.conf; then
    sudo sed -i '/http {/a\\    gzip on;\\n    gzip_vary on;\\n    gzip_comp_level 6;\\n    gzip_types text/plain text/css application/javascript application/json image/svg+xml;' /etc/nginx/nginx.conf
fi
"""
ssh.exec_command(gzip_config)

# Test nginx config
stdin, stdout, stderr = ssh.exec_command('sudo nginx -t')
print('\n--- Nginx config test ---')
print(stderr.read().decode())

# Reload nginx
stdin, stdout, stderr = ssh.exec_command('sudo nginx -s reload')
print('--- Nginx reload ---')
print(stderr.read().decode() or 'Reload OK')

sftp.close()
ssh.close()

print("=" * 60)
print(f"Uploaded: {uploaded} | Errors: {errors}")
print("Done!")
print("=" * 60)
