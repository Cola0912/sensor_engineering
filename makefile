# ターゲットとファイル名の設定
TEXFILE = repo

# デフォルトターゲット
all: $(TEXFILE).pdf

# LaTeXファイルをPDFにコンパイル (xelatex 使用)
$(TEXFILE).pdf: $(TEXFILE).tex
	# ここでxetexを使用して2回コンパイル
	xelatex $(TEXFILE).tex
	xelatex $(TEXFILE).tex  # 目次や参照のために2回目を実行

# クリーンアップ: 中間ファイルを削除
clean:
	rm -f $(TEXFILE).aux $(TEXFILE).log $(TEXFILE).out $(TEXFILE).toc

# distclean: すべての生成物を削除
distclean: clean
	rm -f $(TEXFILE).pdf

# 実行例:
# - make         : PDF を生成
# - make clean   : 中間ファイルを削除
# - make distclean : PDF と中間ファイルをすべて削除
