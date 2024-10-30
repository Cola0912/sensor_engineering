# ターゲットとファイル名の設定
TEXFILE = repo
OUTPUT = HW2_21C1002_相田舟星.pdf  # 学籍番号と名前を含む出力ファイル名

# デフォルトターゲット
all: $(OUTPUT)

# LaTeXファイルをPDFにコンパイル (xelatex 使用)
$(OUTPUT): $(TEXFILE).tex
	# ここでxelatexを使用して2回コンパイル
	xelatex $(TEXFILE).tex
	xelatex $(TEXFILE).tex  # 目次や参照のために2回目を実行
	mv $(TEXFILE).pdf $(OUTPUT)

# クリーンアップ: 中間ファイルを削除
clean:
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out $(TEXFILE).toc

# distclean: すべての生成物を削除
distclean: clean
	rm -f $(OUTPUT)

# 実行例:
# - make         : PDF を生成
# - make clean   : 中間ファイルを削除
# - make distclean : PDF と中間ファイルをすべて削除
