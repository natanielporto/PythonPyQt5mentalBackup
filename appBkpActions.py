import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from appBkp import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.showBtn.clicked.connect(self.actShow)
        self.ui.musicBtn.clicked.connect(self.actMusic)
        self.ui.placeBtn.clicked.connect(self.actPlace)
        self.ui.movieBtn.clicked.connect(self.actMovie)

        self.ui.showListBkp.setHidden(True)
        self.ui.musicListBkp.setHidden(True)
        self.ui.placeListBkp.setHidden(True)
        self.ui.movieListBkp.setHidden(True)

    ###################################################################
    ############################ Music ################################
    ###################################################################

    def actShow(self):

        rdAddShow = self.ui.showRdAdd.isChecked()
        rdRemoveShow = self.ui.showRdRemove.isChecked()
        rdSearchShow = self.ui.showRdSearch.isChecked()
        rdResetShow = self.ui.showRdReset.isChecked()

        name = self.ui.showInput.text()

        if not rdAddShow and not rdRemoveShow and not rdSearchShow and not rdResetShow:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Escolha uma opção antes de acionar a lista de Shows.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return
        else:
            if rdAddShow:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de acrescentar um show é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return
                self.ui.showList.addItem(name)
                self.ui.showInput.setText('')

            if rdRemoveShow:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de remover um show é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.showListBkp.clear()
                numShow = self.ui.showList.count()

                if numShow is 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum show para ser excluído.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                for i in range(numShow):
                    keepShow = self.ui.showList.item(i).text()
                    if name != keepShow:
                        self.ui.showListBkp.addItem(keepShow)

                if self.ui.showListBkp.count() == self.ui.showList.count():
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum show para ser excluído com este nome.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.showList.clear()
                self.ui.showInput.setText('')

                numShowBack = self.ui.showListBkp.count()
                for i in range(numShowBack):
                    keepShow = self.ui.showListBkp.item(i).text()
                    self.ui.showList.addItem(keepShow)

            elif rdSearchShow:
                self.ui.showListBkp.clear()
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Digite nos campos um show para ser encontrado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                numShow = self.ui.showList.count()
                for i in range(numShow):
                    keepShow = self.ui.showList.item(i).text()
                    if name == keepShow:
                        self.ui.showListBkp.addItem(keepShow)

                if self.ui.showListBkp.count() != 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Sucesso!')
                    msg.setText('Parabéns, você já foi ao show pesquisado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.showInput.setText('')
                    return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText('Nenhum show encontrado com estes dados.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.showInput.setText('')
                    return

            elif rdResetShow:
                self.ui.showList.clear()
                self.ui.showListBkp.clear()
                self.ui.showInput.clear()

    ###################################################################
    ############################ Music ################################
    ###################################################################

    def actMusic(self):
        rdAddMusic = self.ui.musicRdAdd.isChecked()
        rdRemoveMusic = self.ui.musicRdRemove.isChecked()
        rdSearchMusic = self.ui.musicRdSearch.isChecked()
        rdResetMusic = self.ui.musicRdReset.isChecked()

        name = self.ui.musicInput.text()

        if not rdAddMusic and not rdRemoveMusic and not rdSearchMusic and not rdResetMusic:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Escolha uma opção antes de acionar a lista de discos ou artistas já assistidos.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return
        else:
            if rdAddMusic:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de acrescentar disco ou artista é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return
                self.ui.musicList.addItem(name)
                self.ui.musicInput.setText('')

            if rdRemoveMusic:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de remover um disco ou artista é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.musicListBkp.clear()
                numMusic = self.ui.musicList.count()

                if numMusic is 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco ou artista para ser excluído.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                for i in range(numMusic):
                    keepMusic = self.ui.musicList.item(i).text()
                    if name != keepMusic:
                        self.ui.musicListBkp.addItem(keepMusic)

                if self.ui.musicListBkp.count() == self.ui.musicList.count():
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco ou artista para ser excluído com este nome.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.musicList.clear()
                self.ui.musicInput.setText('')

                numMusicBack = self.ui.musicListBkp.count()
                for i in range(numMusicBack):
                    keepMusic = self.ui.musicListBkp.item(i).text()
                    self.ui.musicList.addItem(keepMusic)

            elif rdSearchMusic:
                self.ui.musicListBkp.clear()
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco ou artista para ser encontrado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                numMusic = self.ui.musicList.count()
                for i in range(numMusic):
                    keepMusic = self.ui.musicList.item(i).text()
                    if name == keepMusic:
                        self.ui.musicListBkp.addItem(keepMusic)

                if self.ui.musicListBkp.count() != 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Sucesso!')
                    msg.setText('Você já cadastrou este disco ou artista.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.musicInput.setText('')
                    return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Você ainda não cadastrou este disco ou artista.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.musicInput.setText('')
                    return

            elif rdResetMusic:
                self.ui.musicList.clear()
                self.ui.musicListBkp.clear()
                self.ui.musicInput.clear()

    ###################################################################
    ############################ Places ###############################
    ###################################################################

    def actPlace(self):

        rdAddPlace = self.ui.placeRdAdd.isChecked()
        rdRemovePlace = self.ui.placeRdRemove.isChecked()
        rdSearchPlace = self.ui.placeRdSearch.isChecked()
        rdResetPlace = self.ui.placeRdReset.isChecked()

        name = self.ui.placeInput.text()

        if not rdAddPlace and not rdRemovePlace and not rdSearchPlace and not rdResetPlace:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Escolha uma opção antes de acionar a lista de lugares já visitados.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return
        else:
            if rdAddPlace:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de acrescentar um lugar é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return
                self.ui.placeList.addItem(name)
                self.ui.placeInput.setText('')

            if rdRemovePlace:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de remover lugar é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.placeListBkp.clear()
                numPlace = self.ui.placeList.count()

                if numPlace is 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum lugar para ser excluído.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                for i in range(numPlace):
                    keepPlace = self.ui.placeList.item(i).text()
                    if name != keepPlace:
                        self.ui.placeListBkp.addItem(keepPlace)

                if self.ui.placeListBkp.count() == self.ui.placeList.count():
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum lugar para ser excluído com este nome.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.placeList.clear()
                self.ui.placeInput.setText('')

                numPlaceBack = self.ui.placeListBkp.count()
                for i in range(numPlaceBack):
                    keepPlace = self.ui.placeListBkp.item(i).text()
                    self.ui.placeList.addItem(keepPlace)

            elif rdSearchPlace:
                self.ui.placeListBkp.clear()
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum lugar para ser encontrado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                numPlace = self.ui.placeList.count()
                for i in range(numPlace):
                    keepPlace = self.ui.placeList.item(i).text()
                    if name == keepPlace:
                        self.ui.placeListBkp.addItem(keepPlace)

                if self.ui.placeListBkp.count() != 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Sucesso!')
                    msg.setText('Parabéns, você já foi ao lugar pesquisado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.placeInput.setText('')
                    return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText('Nenhum lugar encontrado com estes dados.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.placeInput.setText('')
                    return

            elif rdResetPlace:
                self.ui.placeList.clear()
                self.ui.placeListBkp.clear()
                self.ui.placeInput.clear()

    ###################################################################
    ########################### Movies ################################
    ###################################################################

    def actMovie(self):

        rdAddMovie = self.ui.movieRdAdd.isChecked()
        rdRemoveMovie = self.ui.movieRdRemove.isChecked()
        rdSearchMovie = self.ui.movieRdSearch.isChecked()
        rdResetMovie = self.ui.movieRdReset.isChecked()

        name = self.ui.movieInput.text()

        if not rdAddMovie and not rdRemoveMovie and not rdSearchMovie and not rdResetMovie:
            msg = QMessageBox()
            msg.setWindowTitle('Erro:')
            msg.setText(
                'Escolha uma opção antes de acionar a lista de filmes e seriados já assistidos.')
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            return
        else:
            if rdAddMovie:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de acrescentar um filme ou seriado é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return
                self.ui.movieList.addItem(name)
                self.ui.movieInput.setText('')

            if rdRemoveMovie:
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Antes de remover um disco ou artista é necessário informar qual.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.movieListBkp.clear()
                numMovie = self.ui.movieList.count()

                if numMovie is 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco ou artista para ser excluído.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                for i in range(numMovie):
                    keepMovie = self.ui.movieList.item(i).text()
                    if name != keepMovie:
                        self.ui.movieListBkp.addItem(keepMovie)

                if self.ui.movieListBkp.count() == self.ui.movieList.count():
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum disco ou artista para ser excluído com este nome.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                self.ui.movieList.clear()
                self.ui.movieInput.setText('')

                numMovieBack = self.ui.movieListBkp.count()
                for i in range(numMovieBack):
                    keepMovie = self.ui.movieListBkp.item(i).text()
                    self.ui.movieList.addItem(keepMovie)

            elif rdSearchMovie:
                self.ui.movieListBkp.clear()
                if not name:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Nenhum filme ou seriado para ser encontrado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    return

                numMovie = self.ui.movieList.count()
                for i in range(numMovie):
                    keepMovie = self.ui.movieList.item(i).text()
                    if name == keepMovie:
                        self.ui.movieListBkp.addItem(keepMovie)

                if self.ui.movieListBkp.count() != 0:
                    msg = QMessageBox()
                    msg.setWindowTitle('Sucesso!')
                    msg.setText('Você já assistiu este filme / seriado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.movieInput.setText('')
                    return
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Erro:')
                    msg.setText(
                        'Você ainda não assistiu este filme / seriado.')
                    msg.setIcon(QMessageBox.Question)
                    msg.exec_()
                    self.ui.movieInput.setText('')
                    return

            elif rdResetMovie:
                self.ui.movieList.clear()
                self.ui.movieListBkp.clear()
                self.ui.movieInput.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
