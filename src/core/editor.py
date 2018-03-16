from PyQt5.Qsci import *
from PyQt5.QtGui import QFont, QFontMetrics, QColor

FONT_FAMILY = "Source Code Pro"
BACKGROUND_COLOR = '#f8f8f8'
FOREGROUND_COLOR = '#535353'
MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
MARGIN_FOREGROUND = "#676a6d"
FOLD_MARGIN_BACKGROUND = "#2b2b2b" # "#313335"
EDGE_COLOR = "#BBB8B5"
SEL_BACKGROUND = "#535353" # "#606060"
SEL_FOREGROUND = "#222222"
IND_BACKGROUND = "#676a6d"
IND_FOREGROUND = "#676a6d"
MARKER_BACKGROUND = "#2b2b2b" # "#313335"
MARKER_FOREGROUND = "#676a6d"

use_indentation_markers = False

class Editor(QsciScintilla):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)

        self.bgcolor = '#535353'

        global use_indentation_markers

        ## FONT
        self.font = QFont()
        self.font.setFamily(FONT_FAMILY)
        self.font.setFixedPitch(True)
        self.font.setPointSize(18)
        self.font2 = QFont()
        self.font2.setFamily("Sans-Serif")
        self.font2.setFixedPitch(True)
        self.font2.setPointSize(13)
        self.setFont(self.font)
        self.setMarginsFont(self.font)
        self.setStyleSheet("""
        QsciScintilla
        {
            font-size: 13px !important;
        }
        """)

        # DEFAULT BACKGROUND AND FOREGROUND
        self.setPaper(QColor(BACKGROUND_COLOR))
        self.setColor(QColor(FOREGROUND_COLOR))

        # MARGIN LINE NUMBERS
        fontmetrics = QFontMetrics(self.font)
        self.setMarginsFont(self.font2)
        self.setMarginWidth(0, fontmetrics.width("00000") + 4)
        self.setMarginLineNumbers(0, True)

        # MARGIN BACKGROUND AND FOREGROUND
        self.setMarginsBackgroundColor(QColor(MARGIN_BACKGROUND))
        self.setMarginsForegroundColor(QColor(MARGIN_FOREGROUND))

        # BRACE MATCHING
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # CURRENT LINE
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#f8f8f8"))
        self.setCaretForegroundColor(QColor("#535353"))
        # SELECTION BACKGROUND AND FOREGROUND
        self.setSelectionBackgroundColor(QColor(SEL_BACKGROUND))
        self.setSelectionForegroundColor(QColor(SEL_FOREGROUND))

        # TABS
        self.setIndentationsUseTabs(False)
        self.setIndentationWidth(4)
        self.setTabIndents(True)
        self.setAutoIndent(True)
        self.setBackspaceUnindents(True)
        self.setTabWidth(4)
        # indentation guides
        self.setIndentationGuides(use_indentation_markers)
        # TABS BACKGROUND AND FOREGROUND
        self.setIndentationGuidesBackgroundColor(QColor(IND_BACKGROUND))
        self.setIndentationGuidesForegroundColor(QColor(IND_FOREGROUND))
        # TABS BACKGROUND AND FOREGROUND
        self.setIndentationGuidesBackgroundColor(QColor(IND_BACKGROUND))
        self.setIndentationGuidesForegroundColor(QColor(IND_FOREGROUND))

        # FOLDING MARGIN
        self.setFolding(QsciScintilla.PlainFoldStyle)
        self.setMarginWidth(2, 10) # (2,14)
        # FOLDING MARKERS
        self.markerDefine("V", QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine(">", QsciScintilla.SC_MARKNUM_FOLDER)
        self.markerDefine("V", QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine(">", QsciScintilla.SC_MARKNUM_FOLDEREND)

        # FOLDING MARKERS BACKGROUND AND FOREGROUND
        self.setMarkerBackgroundColor(QColor(MARKER_BACKGROUND))
        self.setMarkerForegroundColor(QColor(MARGIN_FOREGROUND))
        self.setFoldMarginColors(QColor(FOLD_MARGIN_BACKGROUND), QColor(FOLD_MARGIN_BACKGROUND))

        # FOLDING LINE DISABLE
        self.SendScintilla(QsciScintilla.SCI_SETFOLDFLAGS, 0)

        # AUTO COMPLETION
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionThreshold(2)

        # DISABLE HORIZONTAL SCROLLBAR
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        self.setStyleSheet("""
        QsciScintilla
        {
             border: 0px solid black;
             padding: 0px;
             border-radius: 0px;
             opacity: 100;
             font-size: 10px !important;
        }
        """)

