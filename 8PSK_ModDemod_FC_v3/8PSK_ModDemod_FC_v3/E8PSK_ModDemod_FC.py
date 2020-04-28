#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: 8PSK Modulation and Demodulation with Frequency Correction Simulation
# Author: Enrique Quik-e Cametti
# Generated: Sat Mar 14 00:27:41 2020
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import get_first_byte
import numpy as np
import repeat_first_byte
import sip
import sync_decoder
import sync_encoder
import sys
from gnuradio import qtgui


class E8PSK_ModDemod_FC(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "8PSK Modulation and Demodulation with Frequency Correction Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("8PSK Modulation and Demodulation with Frequency Correction Simulation")
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

        self.settings = Qt.QSettings("GNU Radio", "E8PSK_ModDemod_FC")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.RangeRow = RangeRow = 0
        self.BiRow = BiRow = RangeRow+1
        self.ConsRow = ConsRow = BiRow+1
        self.samp_rate = samp_rate = 1e6
        self.nfilts = nfilts = 100
        self.SampSymb = SampSymb = 8
        self.FreqRow = FreqRow = ConsRow+1
        self.FDP = FDP = 0.005
        self.rrc_taps_0 = rrc_taps_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(SampSymb), 0.35, 45*nfilts)
        self.min_PLL = min_PLL = 2*np.pi*(1/float(SampSymb)-1/float(SampSymb)*FDP)
        self.max_PLL = max_PLL = 2*np.pi*(1/float(SampSymb)+1/float(SampSymb)*FDP)
        self.Values = Values = 2
        self.TimeRow = TimeRow = FreqRow+1
        self.SPS = SPS = 2

        self.QPSK_CO = QPSK_CO = digital.constellation_qpsk().base()

        self.Noise = Noise = 0
        self.LBP_PLL = LBP_PLL = (samp_rate/float(SampSymb)-samp_rate/float(SampSymb)*FDP*2)
        self.HBP_PLL = HBP_PLL = (samp_rate/float(SampSymb)+samp_rate/float(SampSymb)*FDP*2)
        self.FreqOff = FreqOff = 0.005

        ##################################################
        # Blocks
        ##################################################
        self._Noise_range = Range(0, 1, 0.01, 0, 200)
        self._Noise_win = RangeWidget(self._Noise_range, self.set_Noise, 'Channel Noise', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Noise_win, 0, 1, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,3)]
        self._FreqOff_range = Range(-1, 1, 0.001, 0.005, 200)
        self._FreqOff_win = RangeWidget(self._FreqOff_range, self.set_FreqOff, 'Frequency Offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._FreqOff_win, 0, 3, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,4)]
        self.sync_encoder = sync_encoder.blk()
        self.sync_decoder = sync_decoder.blk()
        self.repeat_first_byte = repeat_first_byte.blk(repeat=3)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"Original vs Received Data", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.064)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['Original', 'Received', '', '', '',
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 1, 0, 1, 3)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,3)]
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER")

        labels = [' ', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0.set_max(i, 255)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win, 0, 4, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(4,5)]
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("First Byte")

        labels = [' ', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 255)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 0, 5, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(5,6)]
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Pre PSK Demod", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.064)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['Received', 'Mod', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 1, 3, 1, 2)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(1,2)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,5)]
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Post Polyphase Clock", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 3, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Post_Channel_Model", #name
        	3 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Post PLL CPSK', 'Post Filter', 'Pre Filter', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"Pre Polyphase Clock", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.1)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not False:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 2, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.get_first_byte = get_first_byte.blk()
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=8,
          mod_code="gray",
          differential=True,
          samples_per_symbol=SampSymb,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_psk_demod_0 = digital.psk.psk_demod(
          constellation_points=8,
          differential=True,
          samples_per_symbol=SampSymb,
          excess_bw=0.35,
          phase_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(SampSymb, 0.1, (rrc_taps_0), nfilts, nfilts/2, 1.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(.1, 8, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, .01, 2)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=Noise,
        	frequency_offset=FreqOff,
        	epsilon=1.0,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_skiphead_1 = blocks.skiphead(gr.sizeof_char*1, 3)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 31)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_char*1, 5)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=64000,
        	bits_per_symbol=8,
        )
        self.band_pass_filter_0_0 = filter.interp_fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, (2*samp_rate/float(SampSymb)-130e3), (2*samp_rate/float(SampSymb)+100e3), 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_ccf(1, firdes.band_pass(
        	1, samp_rate, 95e3, 105e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 100e3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, 100e3, 1, 0)
        self.analog_pll_refout_cc_0 = analog.pll_refout_cc(0.2, 2*np.pi*103e3/samp_rate, 2*np.pi*97e3/samp_rate)
        self.Video_Source = blocks.file_source(gr.sizeof_char*1, '/home/teddy/Documents/DVB_last_stand/Source_Files/Test_Video.ts', False)
        self.Video_Sink = blocks.file_sink(gr.sizeof_char*1, '/home/teddy/Documents/DVB_last_stand/Received_Files/Test_Video_8PSK_FC_received.ts', False)
        self.Video_Sink.set_unbuffered(True)
        self._Values_range = Range(0, 255, 1, 2, 200)
        self._Values_win = RangeWidget(self._Values_range, self.set_Values, 'Vector Values', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Values_win, 0, 0, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(0,1)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(0,1)]
        self.Post_Polyphase_Clock_Cons = qtgui.const_sink_c(
        	1024, #size
        	'Post Polyphase Clock', #name
        	1 #number of inputs
        )
        self.Post_Polyphase_Clock_Cons.set_update_time(0.10)
        self.Post_Polyphase_Clock_Cons.set_y_axis(-2, 2)
        self.Post_Polyphase_Clock_Cons.set_x_axis(-2, 2)
        self.Post_Polyphase_Clock_Cons.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Post_Polyphase_Clock_Cons.enable_autoscale(False)
        self.Post_Polyphase_Clock_Cons.enable_grid(True)
        self.Post_Polyphase_Clock_Cons.enable_axis_labels(True)

        if not False:
          self.Post_Polyphase_Clock_Cons.disable_legend()

        labels = ['Timing Recov.', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "red"]
        styles = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.5, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Post_Polyphase_Clock_Cons.set_line_label(i, "Data {0}".format(i))
            else:
                self.Post_Polyphase_Clock_Cons.set_line_label(i, labels[i])
            self.Post_Polyphase_Clock_Cons.set_line_width(i, widths[i])
            self.Post_Polyphase_Clock_Cons.set_line_color(i, colors[i])
            self.Post_Polyphase_Clock_Cons.set_line_style(i, styles[i])
            self.Post_Polyphase_Clock_Cons.set_line_marker(i, markers[i])
            self.Post_Polyphase_Clock_Cons.set_line_alpha(i, alphas[i])

        self._Post_Polyphase_Clock_Cons_win = sip.wrapinstance(self.Post_Polyphase_Clock_Cons.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Post_Polyphase_Clock_Cons_win, 2, 1, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(1,2)]
        self.Post_Costas_Loop_Freq = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Post Costas Loop", #name
        	1 #number of inputs
        )
        self.Post_Costas_Loop_Freq.set_update_time(0.10)
        self.Post_Costas_Loop_Freq.set_y_axis(-140, 10)
        self.Post_Costas_Loop_Freq.set_y_label('Relative Gain', 'dB')
        self.Post_Costas_Loop_Freq.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Post_Costas_Loop_Freq.enable_autoscale(False)
        self.Post_Costas_Loop_Freq.enable_grid(False)
        self.Post_Costas_Loop_Freq.set_fft_average(1.0)
        self.Post_Costas_Loop_Freq.enable_axis_labels(True)
        self.Post_Costas_Loop_Freq.enable_control_panel(False)

        if not False:
          self.Post_Costas_Loop_Freq.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.Post_Costas_Loop_Freq.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Post_Costas_Loop_Freq.set_line_label(i, "Data {0}".format(i))
            else:
                self.Post_Costas_Loop_Freq.set_line_label(i, labels[i])
            self.Post_Costas_Loop_Freq.set_line_width(i, widths[i])
            self.Post_Costas_Loop_Freq.set_line_color(i, colors[i])
            self.Post_Costas_Loop_Freq.set_line_alpha(i, alphas[i])

        self._Post_Costas_Loop_Freq_win = sip.wrapinstance(self.Post_Costas_Loop_Freq.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Post_Costas_Loop_Freq_win, 3, 3, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,4)]
        self.Post_Costas_Loop_Cons = qtgui.const_sink_c(
        	1024, #size
        	'Post Costas Loop', #name
        	1 #number of inputs
        )
        self.Post_Costas_Loop_Cons.set_update_time(0.10)
        self.Post_Costas_Loop_Cons.set_y_axis(-2, 2)
        self.Post_Costas_Loop_Cons.set_x_axis(-2, 2)
        self.Post_Costas_Loop_Cons.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Post_Costas_Loop_Cons.enable_autoscale(False)
        self.Post_Costas_Loop_Cons.enable_grid(False)
        self.Post_Costas_Loop_Cons.enable_axis_labels(True)

        if not False:
          self.Post_Costas_Loop_Cons.disable_legend()

        labels = ['Locked', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.6, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Post_Costas_Loop_Cons.set_line_label(i, "Data {0}".format(i))
            else:
                self.Post_Costas_Loop_Cons.set_line_label(i, labels[i])
            self.Post_Costas_Loop_Cons.set_line_width(i, widths[i])
            self.Post_Costas_Loop_Cons.set_line_color(i, colors[i])
            self.Post_Costas_Loop_Cons.set_line_style(i, styles[i])
            self.Post_Costas_Loop_Cons.set_line_marker(i, markers[i])
            self.Post_Costas_Loop_Cons.set_line_alpha(i, alphas[i])

        self._Post_Costas_Loop_Cons_win = sip.wrapinstance(self.Post_Costas_Loop_Cons.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Post_Costas_Loop_Cons_win, 2, 3, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(3,4)]
        self.Post_CMA_Equalizer_Freq = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Post CMA Equalizer", #name
        	1 #number of inputs
        )
        self.Post_CMA_Equalizer_Freq.set_update_time(0.10)
        self.Post_CMA_Equalizer_Freq.set_y_axis(-140, 10)
        self.Post_CMA_Equalizer_Freq.set_y_label('Relative Gain', 'dB')
        self.Post_CMA_Equalizer_Freq.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.Post_CMA_Equalizer_Freq.enable_autoscale(False)
        self.Post_CMA_Equalizer_Freq.enable_grid(False)
        self.Post_CMA_Equalizer_Freq.set_fft_average(1.0)
        self.Post_CMA_Equalizer_Freq.enable_axis_labels(True)
        self.Post_CMA_Equalizer_Freq.enable_control_panel(False)

        if not False:
          self.Post_CMA_Equalizer_Freq.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.Post_CMA_Equalizer_Freq.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Post_CMA_Equalizer_Freq.set_line_label(i, "Data {0}".format(i))
            else:
                self.Post_CMA_Equalizer_Freq.set_line_label(i, labels[i])
            self.Post_CMA_Equalizer_Freq.set_line_width(i, widths[i])
            self.Post_CMA_Equalizer_Freq.set_line_color(i, colors[i])
            self.Post_CMA_Equalizer_Freq.set_line_alpha(i, alphas[i])

        self._Post_CMA_Equalizer_Freq_win = sip.wrapinstance(self.Post_CMA_Equalizer_Freq.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Post_CMA_Equalizer_Freq_win, 3, 2, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(3,4)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,3)]
        self.Post_CMA_Eq_Cons = qtgui.const_sink_c(
        	1024, #size
        	'Post CMA Equalizer', #name
        	1 #number of inputs
        )
        self.Post_CMA_Eq_Cons.set_update_time(0.10)
        self.Post_CMA_Eq_Cons.set_y_axis(-2, 2)
        self.Post_CMA_Eq_Cons.set_x_axis(-2, 2)
        self.Post_CMA_Eq_Cons.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.Post_CMA_Eq_Cons.enable_autoscale(False)
        self.Post_CMA_Eq_Cons.enable_grid(False)
        self.Post_CMA_Eq_Cons.enable_axis_labels(True)

        if not False:
          self.Post_CMA_Eq_Cons.disable_legend()

        labels = ['Equalized', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.6, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.Post_CMA_Eq_Cons.set_line_label(i, "Data {0}".format(i))
            else:
                self.Post_CMA_Eq_Cons.set_line_label(i, labels[i])
            self.Post_CMA_Eq_Cons.set_line_width(i, widths[i])
            self.Post_CMA_Eq_Cons.set_line_color(i, colors[i])
            self.Post_CMA_Eq_Cons.set_line_style(i, styles[i])
            self.Post_CMA_Eq_Cons.set_line_marker(i, markers[i])
            self.Post_CMA_Eq_Cons.set_line_alpha(i, alphas[i])

        self._Post_CMA_Eq_Cons_win = sip.wrapinstance(self.Post_CMA_Eq_Cons.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._Post_CMA_Eq_Cons_win, 2, 2, 1, 1)
        [self.top_grid_layout.setRowStretch(r,1) for r in range(2,3)]
        [self.top_grid_layout.setColumnStretch(c,1) for c in range(2,3)]

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Video_Source, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.analog_pll_refout_cc_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.digital_psk_demod_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.sync_decoder, 0))
        self.connect((self.blocks_skiphead_1, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.blocks_skiphead_1, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_skiphead_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.repeat_first_byte, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.Post_CMA_Eq_Cons, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.Post_CMA_Equalizer_Freq, 0))
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.Post_Costas_Loop_Cons, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.Post_Costas_Loop_Freq, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.Post_Polyphase_Clock_Cons, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.digital_psk_demod_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.digital_psk_mod_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.get_first_byte, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.repeat_first_byte, 0), (self.sync_encoder, 0))
        self.connect((self.sync_decoder, 0), (self.Video_Sink, 0))
        self.connect((self.sync_decoder, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.sync_decoder, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.sync_decoder, 0), (self.get_first_byte, 0))
        self.connect((self.sync_encoder, 0), (self.digital_psk_mod_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "E8PSK_ModDemod_FC")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_RangeRow(self):
        return self.RangeRow

    def set_RangeRow(self, RangeRow):
        self.RangeRow = RangeRow
        self.set_BiRow(self.RangeRow+1)

    def get_BiRow(self):
        return self.BiRow

    def set_BiRow(self, BiRow):
        self.BiRow = BiRow
        self.set_ConsRow(self.BiRow+1)

    def get_ConsRow(self):
        return self.ConsRow

    def set_ConsRow(self, ConsRow):
        self.ConsRow = ConsRow
        self.set_FreqRow(self.ConsRow+1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (2*self.samp_rate/float(self.SampSymb)-130e3), (2*self.samp_rate/float(self.SampSymb)+100e3), 10e3, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 95e3, 105e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_pll_refout_cc_0.set_max_freq(2*np.pi*103e3/self.samp_rate)
        self.analog_pll_refout_cc_0.set_min_freq(2*np.pi*97e3/self.samp_rate)
        self.Post_Costas_Loop_Freq.set_frequency_range(0, self.samp_rate)
        self.Post_CMA_Equalizer_Freq.set_frequency_range(0, self.samp_rate)
        self.set_LBP_PLL((self.samp_rate/float(self.SampSymb)-self.samp_rate/float(self.SampSymb)*self.FDP*2))
        self.set_HBP_PLL((self.samp_rate/float(self.SampSymb)+self.samp_rate/float(self.SampSymb)*self.FDP*2))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.SampSymb), 0.35, 45*self.nfilts))

    def get_SampSymb(self):
        return self.SampSymb

    def set_SampSymb(self, SampSymb):
        self.SampSymb = SampSymb
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.SampSymb), 0.35, 45*self.nfilts))
        self.set_min_PLL(2*np.pi*(1/float(self.SampSymb)-1/float(self.SampSymb)*self.FDP))
        self.set_max_PLL(2*np.pi*(1/float(self.SampSymb)+1/float(self.SampSymb)*self.FDP))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, (2*self.samp_rate/float(self.SampSymb)-130e3), (2*self.samp_rate/float(self.SampSymb)+100e3), 10e3, firdes.WIN_HAMMING, 6.76))
        self.set_LBP_PLL((self.samp_rate/float(self.SampSymb)-self.samp_rate/float(self.SampSymb)*self.FDP*2))
        self.set_HBP_PLL((self.samp_rate/float(self.SampSymb)+self.samp_rate/float(self.SampSymb)*self.FDP*2))

    def get_FreqRow(self):
        return self.FreqRow

    def set_FreqRow(self, FreqRow):
        self.FreqRow = FreqRow
        self.set_TimeRow(self.FreqRow+1)

    def get_FDP(self):
        return self.FDP

    def set_FDP(self, FDP):
        self.FDP = FDP
        self.set_min_PLL(2*np.pi*(1/float(self.SampSymb)-1/float(self.SampSymb)*self.FDP))
        self.set_max_PLL(2*np.pi*(1/float(self.SampSymb)+1/float(self.SampSymb)*self.FDP))
        self.set_LBP_PLL((self.samp_rate/float(self.SampSymb)-self.samp_rate/float(self.SampSymb)*self.FDP*2))
        self.set_HBP_PLL((self.samp_rate/float(self.SampSymb)+self.samp_rate/float(self.SampSymb)*self.FDP*2))

    def get_rrc_taps_0(self):
        return self.rrc_taps_0

    def set_rrc_taps_0(self, rrc_taps_0):
        self.rrc_taps_0 = rrc_taps_0
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps_0))

    def get_min_PLL(self):
        return self.min_PLL

    def set_min_PLL(self, min_PLL):
        self.min_PLL = min_PLL

    def get_max_PLL(self):
        return self.max_PLL

    def set_max_PLL(self, max_PLL):
        self.max_PLL = max_PLL

    def get_Values(self):
        return self.Values

    def set_Values(self, Values):
        self.Values = Values

    def get_TimeRow(self):
        return self.TimeRow

    def set_TimeRow(self, TimeRow):
        self.TimeRow = TimeRow

    def get_SPS(self):
        return self.SPS

    def set_SPS(self, SPS):
        self.SPS = SPS

    def get_QPSK_CO(self):
        return self.QPSK_CO

    def set_QPSK_CO(self, QPSK_CO):
        self.QPSK_CO = QPSK_CO

    def get_Noise(self):
        return self.Noise

    def set_Noise(self, Noise):
        self.Noise = Noise
        self.channels_channel_model_0.set_noise_voltage(self.Noise)

    def get_LBP_PLL(self):
        return self.LBP_PLL

    def set_LBP_PLL(self, LBP_PLL):
        self.LBP_PLL = LBP_PLL

    def get_HBP_PLL(self):
        return self.HBP_PLL

    def set_HBP_PLL(self, HBP_PLL):
        self.HBP_PLL = HBP_PLL

    def get_FreqOff(self):
        return self.FreqOff

    def set_FreqOff(self, FreqOff):
        self.FreqOff = FreqOff
        self.channels_channel_model_0.set_frequency_offset(self.FreqOff)


def main(top_block_cls=E8PSK_ModDemod_FC, options=None):

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
