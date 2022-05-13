from pdf2docx import Converter
import PySimpleGUI as sg


def pdf2word(file_path):
    file_name = file_path.split('.')[0]
    docx_file = f'{file_name}.docx'

    p2w = Converter(file_path)
    p2w.convert(docx_file, start=0, end=None)
    p2w.close()
    return docx_file


def gui():
    sg.theme('BlueMono')

    layout = [
        [sg.Text('PDF to Word', font=("微软雅黑", 12)),
         sg.Text('', key='filename', size=(50, 1), font=("微软雅黑", 10), text_color='green')],
        [sg.Output(size=(80, 10), font=("微软雅黑", 10))],
        [sg.FileBrowse('choose file', key='file', target='filename'), sg.Button('convert'), sg.Button('exit')]
    ]

    window = sg.Window('start', layout, font=("微软雅黑", 15), default_element_size=(50, 1))

    while True:
        event, values = window.read()
        if event in (None, 'exit'):
            break
        if event == 'convert':
            if values['file'] and values['file'].split('.')[1] == 'pdf':
                file_path = pdf2word(values['file'])
                print('\n' + 'conver success' + '\n')
                print(file_path)
            else:
                print('file error!')

    window.close()


if __name__ == '__main__':
    gui()
