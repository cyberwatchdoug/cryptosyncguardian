import subprocess
import logging
import argparse

# Configure logging
logging.basicConfig(filename='cryptosyncguardian.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def rclone_encrypt_and_sync(src_dir, dest, is_remote=False):
    """
    Encrypt and sync a directory using rclone
    
    Parameters:
    - src_dir: Source directory to encrypt and sync
    - dest: Destination directory or remote to sync to
    - is_remote: Boolean indicating if the destination is a remote (default: False)
    """
    if is_remote:
        dest = f'{dest}:'
    
    command = ['rclone', 'sync', src_dir, dest]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode == 0:
            logging.info(f"Sync successful for {src_dir} to {dest}")
        else:
            logging.error(f"Error during sync for {src_dir} to {dest}: {result.stderr.decode('utf-8')}")
    except Exception as e:
        logging.exception(f"Exception occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Encrypt and sync directories using rclone.')
    parser.add_argument('mode', choices=['gdrive', 'local'], help='Mode of operation: gdrive or local')
    parser.add_argument('src', help='Source directory to encrypt and sync')
    parser.add_argument('dest', help='Destination directory or remote to sync to')

    args = parser.parse_args()

    try:
        if args.mode == 'gdrive':
            logging.info(f"Starting sync from {args.src} to Google Drive remote {args.dest}")
            rclone_encrypt_and_sync(args.src, args.dest, is_remote=True)
        elif args.mode == 'local':
            logging.info(f"Starting sync from {args.src} to local directory {args.dest}")
            rclone_encrypt_and_sync(args.src, args.dest)
    except Exception as e:
        logging.exception(f"Failed to sync: {e}")
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()