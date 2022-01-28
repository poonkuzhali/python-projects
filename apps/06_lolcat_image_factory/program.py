import os.path

import service


def main():
    header()
    cat_service()


def header():
    print('-------------------------------------')
    print('         LOL CAT APP')
    print('-------------------------------------')


def cat_service():
    folder = 'cat_images'
    path = os.path.abspath(os.path.join(os.getcwd(), folder))
    print(path)
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(1, 10):
        print('Downloading cat image {}'.format(str(i)))
        data = service.get_random_cat_image()
        service.save_image(data, path, 'cat_img_' + str(i))
    print('Opening folder in finder....')
    service.open_folder(folder)


if __name__ == '__main__':
    main()
