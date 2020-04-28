#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Video Codif and Decodif
# Author: Enrique 'Quik-e' Cametti
# Description: Working Flowchart of DVB-S codification and decodification
# Generated: Wed Mar  4 20:52:49 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class DVB_Cod(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Video Codif and Decodif")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Video Codif and Decodif")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "DVB_Cod")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e6

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	188*10, #size
        	samp_rate, #samp_rate
        	"File Sink", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Byte Value', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['Byte given to file sink', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.dtv_dvbt_viterbi_decoder_0 = dtv.dvbt_viterbi_decoder(dtv.MOD_QPSK, dtv.NH, dtv.C5_6, 1512*4)
        self.dtv_dvbt_reed_solomon_enc_0 = dtv.dvbt_reed_solomon_enc(2, 8, 0x11d, 255, 239, 8, 51, 8)
        self.dtv_dvbt_reed_solomon_dec_0 = dtv.dvbt_reed_solomon_dec(2, 8, 0x11d, 255, 239, 8, 51, 8)
        self.dtv_dvbt_inner_coder_0 = dtv.dvbt_inner_coder(1, 1512*4, dtv.MOD_QPSK, dtv.NH, dtv.C5_6)
        self.dtv_dvbt_energy_dispersal_0 = dtv.dvbt_energy_dispersal(1)
        self.dtv_dvbt_energy_descramble_0 = dtv.dvbt_energy_descramble(1504/188)
        self.dtv_dvbt_convolutional_interleaver_0 = dtv.dvbt_convolutional_interleaver(136, 12, 17)
        self.dtv_dvbt_convolutional_deinterleaver_0 = dtv.dvbt_convolutional_deinterleaver(136, 12, 17)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_char*1, 6048)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/teddy/Documents/DVB_last_stand/Received_Files/Test_Video_CodDecod_received.ts', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.Video_Source = blocks.file_source(gr.sizeof_char*1, '/home/teddy/Documents/DVB_last_stand/Source_Files/Test_Video.ts', False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Video_Source, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.dtv_dvbt_energy_dispersal_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.dtv_dvbt_viterbi_decoder_0, 0))
        self.connect((self.dtv_dvbt_convolutional_deinterleaver_0, 0), (self.dtv_dvbt_reed_solomon_dec_0, 0))
        self.connect((self.dtv_dvbt_convolutional_interleaver_0, 0), (self.dtv_dvbt_inner_coder_0, 0))
        self.connect((self.dtv_dvbt_energy_descramble_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.dtv_dvbt_energy_descramble_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.dtv_dvbt_energy_dispersal_0, 0), (self.dtv_dvbt_reed_solomon_enc_0, 0))
        self.connect((self.dtv_dvbt_inner_coder_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.dtv_dvbt_reed_solomon_dec_0, 0), (self.dtv_dvbt_energy_descramble_0, 0))
        self.connect((self.dtv_dvbt_reed_solomon_enc_0, 0), (self.dtv_dvbt_convolutional_interleaver_0, 0))
        self.connect((self.dtv_dvbt_viterbi_decoder_0, 0), (self.dtv_dvbt_convolutional_deinterleaver_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DVB_Cod")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=DVB_Cod, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
