import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from boss import load_bosses_from_json
from PythonProject.darksoulsAPP_ui import Ui_MainWindow
import json

def save_bosses_to_json(bosses, file_path="data/databoss.json"):
    with open(file_path, "w", encoding="utf-8") as f:
        boss_data = {
            name: {
                "location": boss.location,
                "difficulty": boss.difficulty,
                "weaknesses": boss.weaknesses,
                "lore": boss.lore,
                "prerequisites": boss.prerequisites,
                "defeated": boss.defeated,
                "phase_tips": boss.phase_tips,
                "image": boss.image
            } for name, boss in bosses.items()
        }
        json.dump(boss_data, f, indent=4)

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.boss_data = load_bosses_from_json("data/databoss.json")
        self.total_bosses = 15

        self.defeated_count = sum(1 for boss in self.boss_data.values() if boss.defeated)
        self.ui.progressBar.setValue(int((self.defeated_count / self.total_bosses) * 100))

        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("music/main_theme.wav")))
        self.ui.playButton.clicked.connect(self.toggle_music)
        self.ui.resetButton.clicked.connect(self.reset_progress)

        self.ui.textLore.setHtml(
            '<div align="center">'
            '<h1 style="color:#FFD700; font-family:\'Trajan Pro\';">DARK SOULS III</h1>'
            '<p style="color:white; font-size:14pt;">Prepare to die... again.</p>'
            '</div>'
        )

        self.ui.bossList.itemSelectionChanged.connect(self.display_boss_info)
        self.ui.defeatBox.setChecked(False)
        self.ui.defeatBox.stateChanged.connect(self.handle_defeat_box)
        self.ui.tipBox.stateChanged.connect(self.show_tips_popup)

    def reset_progress(self):
        confirmation = QtWidgets.QMessageBox.question(
            self,
            "Reset Progress",
            "Are you sure you want to reset all progress?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        if confirmation == QtWidgets.QMessageBox.Yes:
            self.defeated_count = 0
            for boss in self.boss_data.values():
                boss.defeated = False
            save_bosses_to_json(self.boss_data)
            self.ui.progressBar.setValue(0)
            self.ui.defeatBox.blockSignals(True)
            self.ui.defeatBox.setChecked(False)
            self.ui.defeatBox.blockSignals(False)
            self.display_boss_info()
            QtWidgets.QMessageBox.information(self, "Reset", "All progress has been reset.")

    def display_boss_info(self):
        selected_items = self.ui.bossList.selectedItems()
        if not selected_items:
            self.ui.textLore.setHtml(
                '<div align="center">'
                '<h1 style="color:#FFD700; font-family:\'Trajan Pro\';">DARK SOULS III</h1>'
                '<p style="color:white; font-size:14pt;">Prepare to die... again.</p>'
                '</div>'
            )
            self.ui.label_2.clear()
            self.ui.defeatBox.blockSignals(True)
            self.ui.defeatBox.setChecked(False)
            self.ui.defeatBox.blockSignals(False)
            return

        boss_name = selected_items[0].text()
        boss = self.boss_data.get(boss_name)

        self.ui.textLore.setText(boss.lore)

        pixmap = QtGui.QPixmap(boss.image)
        if not pixmap.isNull():
            self.ui.label_2.setPixmap(pixmap.scaled(
                self.ui.label_2.size(),
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            ))
        else:
            self.ui.label_2.setText("Image not found.")
            self.ui.label_2.setPixmap(QtGui.QPixmap())

        self.ui.defeatBox.blockSignals(True)
        self.ui.defeatBox.setChecked(boss.defeated)
        self.ui.defeatBox.blockSignals(False)

    def handle_defeat_box(self):
        selected_items = self.ui.bossList.selectedItems()
        if not selected_items:
            return

        boss_name = selected_items[0].text()
        boss = self.boss_data.get(boss_name)
        if not boss:
            return

        selected_index = self.ui.bossList.currentRow()

        if self.ui.defeatBox.isChecked():
            if selected_index > 1:
                prev_boss_name = self.ui.bossList.item(selected_index - 1).text()
                if prev_boss_name != "Select a Boss" and not self.boss_data[prev_boss_name].defeated:
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Defeat Order Violation",
                        f"You must defeat:\n→ {prev_boss_name} first."
                    )
                    self.ui.defeatBox.blockSignals(True)
                    self.ui.defeatBox.setChecked(False)
                    self.ui.defeatBox.blockSignals(False)
                    return

            missing = [pr for pr in boss.prerequisites if not self.boss_data[pr].defeated]
            if missing:
                QtWidgets.QMessageBox.warning(
                    self, "Missing Prerequisite",
                    "Must beat the following boss(es) first:\n" + "\n".join(missing)
                )
                for i in range(self.ui.bossList.count()):
                    if self.ui.bossList.item(i).text() == missing[0]:
                        self.ui.bossList.setCurrentRow(i)
                        break
                self.ui.defeatBox.blockSignals(True)
                self.ui.defeatBox.setChecked(False)
                self.ui.defeatBox.blockSignals(False)
                return

            if not boss.defeated:
                boss.defeated = True
                self.defeated_count += 1
                self.ui.progressBar.setValue(int((self.defeated_count / 15) * 100))
                save_bosses_to_json(self.boss_data)

                lords_of_cinder = [
                    "Lorian, Elder Prince and Lothric, Younger Prince",
                    "Soul of Cinder",
                    "Aldrich, Devourer of Gods",
                    "Yhorm the Giant",
                    "Abyss Watchers",
                ]

                if boss_name in lords_of_cinder:
                    self.show_boss_popup("LORD OF CINDER FALLEN")
                else:
                    self.show_boss_popup("HEIR OF FIRE DESTROYED")

                if self.defeated_count == 15:
                    self.show_boss_popup("VICTORY ACHIEVED")
                    self.show_boss_popup("The five lords sit their five thrones.<br>All thanks to thee, most worthy of lords.")

        else:
            if boss.defeated:
                boss.defeated = False
                self.defeated_count -= 1
                self.ui.progressBar.setValue(int((self.defeated_count / 15) * 100))
                save_bosses_to_json(self.boss_data)

    def show_tips_popup(self):
        if not self.ui.tipBox.isChecked():
            return

        selected_items = self.ui.bossList.selectedItems()
        if not selected_items:
            self.ui.tipBox.setChecked(False)
            return

        boss_name = selected_items[0].text()
        boss = self.boss_data.get(boss_name)
        if not boss:
            self.ui.tipBox.setChecked(False)
            return

        location = boss.location
        difficulty = boss.difficulty
        weaknesses = ", ".join(boss.weaknesses) if boss.weaknesses else "None"
        phase_1 = boss.phase_tips.get("phase_1", "No tips for phase 1.")
        phase_2 = boss.phase_tips.get("phase_2", "No tips for phase 2.")

        message = f"""
        <b>{boss_name}</b><br>
        <b>Location:</b> {location}<br>
        <b>Difficulty:</b> {difficulty}/10<br>
        <b>Weaknesses:</b> {weaknesses}<br>
        <b>Phase 1:</b> {phase_1}<br>
        <b>Phase 2:</b> {phase_2}
        """

        popup = QtWidgets.QDialog(self)
        popup.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        popup.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        popup.setModal(True)

        label = QtWidgets.QLabel(message)
        label.setTextFormat(QtCore.Qt.RichText)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-family: "Trajan Pro";
                font-size: 16px;
                background-color: rgba(0, 0, 0, 230);
                border: 2px solid #FFD700;
                border-radius: 12px;
                padding: 20px;
            }
        """)
        label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        close_btn = QtWidgets.QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #222;
                color: #FFD700;
                font-family: "Trajan Pro";
                font-size: 14px;
                padding: 10px 20px;
                border: 1px solid #FFD700;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #333;
            }
        """)
        close_btn.clicked.connect(popup.accept)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addSpacing(10)
        layout.addWidget(close_btn, alignment=QtCore.Qt.AlignCenter)
        popup.setLayout(layout)

        popup.resize(520, 300)
        popup.move(
            self.geometry().center().x() - popup.width() // 2,
            self.geometry().center().y() - popup.height() // 2
        )

        popup.exec_()

        self.ui.tipBox.blockSignals(True)
        self.ui.tipBox.setChecked(False)
        self.ui.tipBox.blockSignals(False)

    def show_boss_popup(self, message):
        popup = QtWidgets.QDialog(self)
        popup.setWindowTitle("Notice")
        popup.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
        popup.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        popup.setModal(True)

        label = QtWidgets.QLabel(message, popup)
        label.setTextFormat(QtCore.Qt.RichText)
        label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-family: Arial, sans-serif;
                font-size: 20px;
                font-weight: bold;
                background-color: rgba(30, 30, 30, 230);
                border: 2px solid #888;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        label.setAlignment(QtCore.Qt.AlignCenter)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        popup.setLayout(layout)

        popup.resize(520, 120)
        popup.move(
            self.geometry().center().x() - popup.width() // 2,
            self.geometry().center().y() - popup.height() // 2
        )

        if message == "VICTORY ACHIEVED" or "The five lords" in message:
            duration = 3000
        else:
            duration = 1500

        QtCore.QTimer.singleShot(duration, popup.accept)
        popup.exec_()

    def toggle_music(self):
        if self.media_player.state() == QMediaPlayer.PlayingState:
            self.media_player.stop()
        else:
            self.media_player.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
