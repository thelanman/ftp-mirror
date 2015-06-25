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
    import sys
    from ftplib import FTP

    src_path, dst_path = sys.argv[2], sys.argv[3]
    ip, port = sys.argv[1].split(':')
    ftp = FTP()
    ftp.connect(ip, int(port))
    ftp.login()
    ftp.cwd(src_path)
    files = ftp.nlst()
    new = backup_files(ftp, dst_path, files)
    print 'Backup Complete\nNew: %d\nOld: %d' % (new, len(files) - new)
