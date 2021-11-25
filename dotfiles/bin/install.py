#!/usr/bin/env python3

from os.path import expanduser
import datetime
import os
import platform
import subprocess
import shutil
import sys
import glob


# 指定したディレクトリ内のファイル一覧を取得する
def list_dotfiles(directory):
    files = glob.glob(directory + "/.*")
    return files


def main():
    # ホームディレクトリを取得
    home = expanduser("~")
    old_dotfiles = list_dotfiles(home)

    # backupディレクトリの作成
    now_date = (datetime.datetime.now()).strftime('%Y%m%d%H%M')
    dotfiles_backup_dir = home + '/dotfiles_backup/' + now_date
    os.makedirs(dotfiles_backup_dir, exist_ok=True)

#    # dotfileをバックアップ
#    for f in old_dotfiles:
#        shutil.move(f, dotfiles_backup_dir)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_script_dir = os.path.join(os.path.dirname(script_dir), './')
    parent_script_dir = os.path.normpath(parent_script_dir)
    new_dotfiles = list_dotfiles(parent_script_dir)

    with open(os.path.join(parent_script_dir, '.gitignore_global'), "r") as f:
        list = f.read().split('\n')
        # シンボリックリンク作成
        for n in new_dotfiles:
            basename = os.path.basename(n)
            if basename not in list:
                link_path = os.path.join(home, basename)

                if os.path.exists(link_path):
                    shutil.move(link_path, dotfiles_backup_dir)

                os.symlink(n, link_path)

    # Mac
    if platform.system() == 'Darwin':
        print(platform.system())

    # Windows
    if platform.system() == 'Windows':
        print(platform.system())

    # Linux
    if platform.system() == 'Linux':
        print(platform.system())

    # コマンド実行
    command = []
    command.append(['git', 'config', '--global', 'core.excludesfile',
                    os.path.join(home, 'common/.gitignore_global')])

    for c in command:
        subprocess.call(c)


if __name__ == '__main__':
    main()
