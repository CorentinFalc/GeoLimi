# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\observation_ajout_edition_form.ui'
#
# Created: Mon Apr 02 13:51:00 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_observation_ajout_edition_form(object):
    def setupUi(self, observation_ajout_edition_form):
        observation_ajout_edition_form.setObjectName(_fromUtf8("observation_ajout_edition_form"))
        observation_ajout_edition_form.resize(390, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(observation_ajout_edition_form.sizePolicy().hasHeightForWidth())
        observation_ajout_edition_form.setSizePolicy(sizePolicy)
        observation_ajout_edition_form.setMinimumSize(QtCore.QSize(390, 500))
        observation_ajout_edition_form.setMaximumSize(QtCore.QSize(390, 700))
        self.verticalLayout_5 = QtGui.QVBoxLayout(observation_ajout_edition_form)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(observation_ajout_edition_form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_obs_id = QtGui.QLineEdit(observation_ajout_edition_form)
        self.le_obs_id.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_obs_id.sizePolicy().hasHeightForWidth())
        self.le_obs_id.setSizePolicy(sizePolicy)
        self.le_obs_id.setMinimumSize(QtCore.QSize(50, 0))
        self.le_obs_id.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.le_obs_id.setFont(font)
        self.le_obs_id.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);background-color: rgb(255, 255, 255);"))
        self.le_obs_id.setText(_fromUtf8(""))
        self.le_obs_id.setAlignment(QtCore.Qt.AlignCenter)
        self.le_obs_id.setObjectName(_fromUtf8("le_obs_id"))
        self.horizontalLayout.addWidget(self.le_obs_id)
        self.label_5 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.de_obs_date = QtGui.QDateEdit(observation_ajout_edition_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_obs_date.sizePolicy().hasHeightForWidth())
        self.de_obs_date.setSizePolicy(sizePolicy)
        self.de_obs_date.setMinimumSize(QtCore.QSize(85, 20))
        self.de_obs_date.setCalendarPopup(True)
        self.de_obs_date.setObjectName(_fromUtf8("de_obs_date"))
        self.horizontalLayout.addWidget(self.de_obs_date)
        self.label_6 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.te_obs_heure = QtGui.QTimeEdit(observation_ajout_edition_form)
        self.te_obs_heure.setObjectName(_fromUtf8("te_obs_heure"))
        self.horizontalLayout.addWidget(self.te_obs_heure)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.chk_obs_verifiee = QtGui.QCheckBox(observation_ajout_edition_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_obs_verifiee.sizePolicy().hasHeightForWidth())
        self.chk_obs_verifiee.setSizePolicy(sizePolicy)
        self.chk_obs_verifiee.setMinimumSize(QtCore.QSize(0, 20))
        self.chk_obs_verifiee.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.chk_obs_verifiee.setObjectName(_fromUtf8("chk_obs_verifiee"))
        self.verticalLayout_5.addWidget(self.chk_obs_verifiee)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_10 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_2.addWidget(self.label_10)
        self.cmb_obs_cycle_id = QtGui.QComboBox(observation_ajout_edition_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_obs_cycle_id.sizePolicy().hasHeightForWidth())
        self.cmb_obs_cycle_id.setSizePolicy(sizePolicy)
        self.cmb_obs_cycle_id.setMinimumSize(QtCore.QSize(76, 20))
        self.cmb_obs_cycle_id.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cmb_obs_cycle_id.setObjectName(_fromUtf8("cmb_obs_cycle_id"))
        self.horizontalLayout_2.addWidget(self.cmb_obs_cycle_id)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(42, -1, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_11 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_3.addWidget(self.label_11)
        self.cmb_obs_tyact_id = QtGui.QComboBox(observation_ajout_edition_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_obs_tyact_id.sizePolicy().hasHeightForWidth())
        self.cmb_obs_tyact_id.setSizePolicy(sizePolicy)
        self.cmb_obs_tyact_id.setMinimumSize(QtCore.QSize(76, 20))
        self.cmb_obs_tyact_id.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cmb_obs_tyact_id.setObjectName(_fromUtf8("cmb_obs_tyact_id"))
        self.horizontalLayout_3.addWidget(self.cmb_obs_tyact_id)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_12 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_4.addWidget(self.label_12)
        self.sp_obs_searching_time = QtGui.QSpinBox(observation_ajout_edition_form)
        self.sp_obs_searching_time.setObjectName(_fromUtf8("sp_obs_searching_time"))
        self.horizontalLayout_4.addWidget(self.sp_obs_searching_time)
        spacerItem = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_13 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.sp_obs_gps_voltage = QtGui.QDoubleSpinBox(observation_ajout_edition_form)
        self.sp_obs_gps_voltage.setObjectName(_fromUtf8("sp_obs_gps_voltage"))
        self.horizontalLayout_5.addWidget(self.sp_obs_gps_voltage)
        self.label_14 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.sp_obs_gps_temperature = QtGui.QSpinBox(observation_ajout_edition_form)
        self.sp_obs_gps_temperature.setObjectName(_fromUtf8("sp_obs_gps_temperature"))
        self.horizontalLayout_5.addWidget(self.sp_obs_gps_temperature)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_15 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        self.sp_obs_distance_points = QtGui.QDoubleSpinBox(observation_ajout_edition_form)
        self.sp_obs_distance_points.setDecimals(4)
        self.sp_obs_distance_points.setObjectName(_fromUtf8("sp_obs_distance_points"))
        self.horizontalLayout_6.addWidget(self.sp_obs_distance_points)
        self.label_16 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_6.addWidget(self.label_16)
        self.sp_obs_speed = QtGui.QDoubleSpinBox(observation_ajout_edition_form)
        self.sp_obs_speed.setDecimals(4)
        self.sp_obs_speed.setObjectName(_fromUtf8("sp_obs_speed"))
        self.horizontalLayout_6.addWidget(self.sp_obs_speed)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_17 = QtGui.QLabel(observation_ajout_edition_form)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_12.addWidget(self.label_17)
        self.le_fich_chemin = QtGui.QLineEdit(observation_ajout_edition_form)
        self.le_fich_chemin.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_fich_chemin.sizePolicy().hasHeightForWidth())
        self.le_fich_chemin.setSizePolicy(sizePolicy)
        self.le_fich_chemin.setMinimumSize(QtCore.QSize(300, 0))
        self.le_fich_chemin.setMaximumSize(QtCore.QSize(1666666, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.le_fich_chemin.setFont(font)
        self.le_fich_chemin.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);background-color: rgb(255, 255, 255);"))
        self.le_fich_chemin.setText(_fromUtf8(""))
        self.le_fich_chemin.setAlignment(QtCore.Qt.AlignCenter)
        self.le_fich_chemin.setObjectName(_fromUtf8("le_fich_chemin"))
        self.horizontalLayout_12.addWidget(self.le_fich_chemin)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.groupBox = QtGui.QGroupBox(observation_ajout_edition_form)
        self.groupBox.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lbl_vent = QtGui.QLabel(self.groupBox)
        self.lbl_vent.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_vent.setText(_fromUtf8(""))
        self.lbl_vent.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_vent.setObjectName(_fromUtf8("lbl_vent"))
        self.horizontalLayout_7.addWidget(self.lbl_vent)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lbl_direction_v = QtGui.QLabel(self.groupBox)
        self.lbl_direction_v.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_direction_v.setText(_fromUtf8(""))
        self.lbl_direction_v.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_direction_v.setObjectName(_fromUtf8("lbl_direction_v"))
        self.horizontalLayout_7.addWidget(self.lbl_direction_v)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.lbl_nebu = QtGui.QLabel(self.groupBox)
        self.lbl_nebu.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_nebu.setText(_fromUtf8(""))
        self.lbl_nebu.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nebu.setObjectName(_fromUtf8("lbl_nebu"))
        self.horizontalLayout_8.addWidget(self.lbl_nebu)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lbl_tempe = QtGui.QLabel(self.groupBox)
        self.lbl_tempe.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_tempe.setText(_fromUtf8(""))
        self.lbl_tempe.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tempe.setObjectName(_fromUtf8("lbl_tempe"))
        self.horizontalLayout_8.addWidget(self.lbl_tempe)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(observation_ajout_edition_form)
        self.groupBox_2.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lbl_coef_mar = QtGui.QLabel(self.groupBox_2)
        self.lbl_coef_mar.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_coef_mar.setText(_fromUtf8(""))
        self.lbl_coef_mar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_coef_mar.setObjectName(_fromUtf8("lbl_coef_mar"))
        self.horizontalLayout_9.addWidget(self.lbl_coef_mar)
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lbl_marnage = QtGui.QLabel(self.groupBox_2)
        self.lbl_marnage.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0)"))
        self.lbl_marnage.setText(_fromUtf8(""))
        self.lbl_marnage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_marnage.setObjectName(_fromUtf8("lbl_marnage"))
        self.horizontalLayout_9.addWidget(self.lbl_marnage)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_10.addWidget(self.label_18)
        self.lbl_position_maree = QtGui.QLabel(self.groupBox_2)
        self.lbl_position_maree.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_position_maree.setText(_fromUtf8(""))
        self.lbl_position_maree.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position_maree.setObjectName(_fromUtf8("lbl_position_maree"))
        self.horizontalLayout_10.addWidget(self.lbl_position_maree)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(observation_ajout_edition_form)
        self.groupBox_3.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_19 = QtGui.QLabel(self.groupBox_3)
        self.label_19.setStyleSheet(_fromUtf8("color: rgb(107, 107, 107);"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_11.addWidget(self.label_19)
        self.lbl_phase_lune = QtGui.QLabel(self.groupBox_3)
        self.lbl_phase_lune.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.lbl_phase_lune.setText(_fromUtf8(""))
        self.lbl_phase_lune.setObjectName(_fromUtf8("lbl_phase_lune"))
        self.horizontalLayout_11.addWidget(self.lbl_phase_lune)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        spacerItem4 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.btnBox = QtGui.QDialogButtonBox(observation_ajout_edition_form)
        self.btnBox.setMinimumSize(QtCore.QSize(0, 30))
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.btnBox.setCenterButtons(True)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout_5.addWidget(self.btnBox)

        self.retranslateUi(observation_ajout_edition_form)
        QtCore.QMetaObject.connectSlotsByName(observation_ajout_edition_form)

    def retranslateUi(self, observation_ajout_edition_form):
        observation_ajout_edition_form.setWindowTitle(_translate("observation_ajout_edition_form", "Geolimi - Observation - Ajout / Edition", None))
        self.label.setText(_translate("observation_ajout_edition_form", "Id", None))
        self.label_5.setText(_translate("observation_ajout_edition_form", "Date", None))
        self.label_6.setText(_translate("observation_ajout_edition_form", "Heure", None))
        self.chk_obs_verifiee.setText(_translate("observation_ajout_edition_form", "Observation vérifiée", None))
        self.label_10.setText(_translate("observation_ajout_edition_form", "Cycle biologique", None))
        self.label_11.setText(_translate("observation_ajout_edition_form", "Activité", None))
        self.label_12.setText(_translate("observation_ajout_edition_form", "Searching time", None))
        self.label_13.setText(_translate("observation_ajout_edition_form", "Voltage GPS", None))
        self.label_14.setText(_translate("observation_ajout_edition_form", "Température GPS", None))
        self.label_15.setText(_translate("observation_ajout_edition_form", "Distance points", None))
        self.label_16.setText(_translate("observation_ajout_edition_form", "Speed", None))
        self.label_17.setText(_translate("observation_ajout_edition_form", "Fichier", None))
        self.groupBox.setTitle(_translate("observation_ajout_edition_form", "Meteo", None))
        self.label_2.setText(_translate("observation_ajout_edition_form", "Force du vent : ", None))
        self.label_4.setText(_translate("observation_ajout_edition_form", "Direction du vent : ", None))
        self.label_3.setText(_translate("observation_ajout_edition_form", "Nebulosité : ", None))
        self.label_7.setText(_translate("observation_ajout_edition_form", "Température : ", None))
        self.groupBox_2.setTitle(_translate("observation_ajout_edition_form", "Marée", None))
        self.label_8.setText(_translate("observation_ajout_edition_form", "Coeficient : ", None))
        self.label_9.setText(_translate("observation_ajout_edition_form", "Marnage : ", None))
        self.label_18.setText(_translate("observation_ajout_edition_form", "Position : ", None))
        self.groupBox_3.setTitle(_translate("observation_ajout_edition_form", "Lune", None))
        self.label_19.setText(_translate("observation_ajout_edition_form", "Phase de lune : ", None))

import resourcesGeolimi_rc