import os


def notification(message, title):
    command = f'''
    osascript -e 'display notification "{message}" with title "{title}"'
    '''
    os.system(command)


if __name__ == '__main__':
    notification('ggggnwgnrgntg', 'title')
