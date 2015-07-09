import os


def backup(ftp, path, fn):
    dst_path = path + os.path.sep + fn
    if not os.path.isfile(path + os.path.sep + fn):
        ftp.retrbinary('RETR ' + fn, open(path + os.path.sep + fn, 'wb').write)
        return True
    return False


def backup_files(ftp, path, files):
    new = 0
    for fn in files:
        found_new = backup(ftp, path, fn)
        if found_new:
            new += 1
    return new


if __name__ == "__main__":
    import argparse
    import sys
    from ftplib import FTP

    parser = argparse.ArgumentParser(description='Sync a remote FTP server to local storage')
    parser.add_argument('ip', type=str, help='IPv4 address of remote FTP server')
    parser.add_argument('--port', type=int, help='port number of remote FTP server (default=21)', default=21)
    parser.add_argument('src_path', type=str, help='source path on remote FTP server')
    parser.add_argument('dst_path', type=str, help='local path to save remotely downloaded files')
    args = parser.parse_args()

    ftp = FTP()
    ftp.connect(args.ip, args.port)
    ftp.login()
    ftp.cwd(args.src_path)
    files = ftp.nlst()
    new = backup_files(ftp, args.dst_path, files)
    print 'Backup Complete\nNew: %d\nOld: %d' % (new, len(files) - new)
