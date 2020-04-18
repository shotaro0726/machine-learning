{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/anaconda3/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-ef4c5cfe97f3>\", line 9, in dirdialog_clicked\n",
      "    iDir = os.path.abspath(os.path.dirname(__file__))\n",
      "NameError: name '__file__' is not defined\n",
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/anaconda3/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-ef4c5cfe97f3>\", line 9, in dirdialog_clicked\n",
      "    iDir = os.path.abspath(os.path.dirname(__file__))\n",
      "NameError: name '__file__' is not defined\n",
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/opt/anaconda3/lib/python3.7/tkinter/__init__.py\", line 1705, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"<ipython-input-1-ef4c5cfe97f3>\", line 9, in dirdialog_clicked\n",
      "    iDir = os.path.abspath(os.path.dirname(__file__))\n",
      "NameError: name '__file__' is not defined\n"
     ]
    }
   ],
   "source": [
    "import os,sys\n",
    "from tkinter import * \n",
    "from tkinter import ttk\n",
    "from tkinter import messagebox\n",
    "from tkinter import filedialog\n",
    "\n",
    "\n",
    "def dirdialog_clicked():\n",
    "    iDir = os.path.abspath(os.path.dirname(__file__))\n",
    "    iDirPath = filedialog.askdirectory(initialdir= iDir)\n",
    "    entry1.set(iDirPath)\n",
    "\n",
    "def filedialog_clicked():\n",
    "    fType=[(\"\",\"*\")]\n",
    "    iFile = os.path.abspath(os.path.dirname(__file__))\n",
    "    iFilePath = filedialog.askopenfilename(filetype= fType, initialdir = iFile)\n",
    "    entry2.set(iFilePath)\n",
    "\n",
    "def conductMain():\n",
    "    text = \"\"\n",
    "    \n",
    "    dirPath = entry1.get()\n",
    "    filePath = entry2.get()\n",
    "    if dirPath:\n",
    "        text += \"フォルダパス:\" + dirPath + \"\\n\"\n",
    "    if filePath:\n",
    "        text += \"ファイルパス\" + filePath\n",
    "    \n",
    "    if text:\n",
    "        messagebox.showinfo(\"info\", text)\n",
    "    else:\n",
    "        messagebox.showerror(\"error\",\"パスの指定がありません\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    \n",
    "    root = Tk()\n",
    "    root.title(\"翔太郎のふぁいるけんさく\")\n",
    "    \n",
    "    frame1 = ttk.Frame(root, padding=10)\n",
    "    frame1.grid(row=0, column=1, sticky=E)\n",
    "    \n",
    "    IDirLabel = ttk.Label(frame1, text=\"フォルダ参照>>\",padding=(5,2))\n",
    "    IDirLabel.pack(side=LEFT)\n",
    "    \n",
    "    entry1 = StringVar()\n",
    "    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)\n",
    "    IDirEntry.pack(side=LEFT)\n",
    "    \n",
    "    IDirButton = ttk.Button(frame1, text=\"参照\", command=dirdialog_clicked)\n",
    "    IDirButton.pack(side=LEFT)\n",
    "    \n",
    "    frame2 = ttk.Frame(root, padding=10)\n",
    "    frame2.grid(row=2, column=1, sticky=E)\n",
    "    \n",
    "    IDirLabel = ttk.Label(frame2, text=\"ファイル参照>>\",padding=(5,2))\n",
    "    IDirLabel.pack(side=LEFT)\n",
    "    \n",
    "    entry2 = StringVar()\n",
    "    IDirEntry = ttk.Entry(frame1, textvariable=entry2, width=30)\n",
    "    IDirEntry.pack(side=LEFT)\n",
    "    \n",
    "    IDirButton = ttk.Button(frame2, text=\"参照\", command=dirdialog_clicked)\n",
    "    IDirButton.pack(side=LEFT)\n",
    "    \n",
    "    frame3 = ttk.Frame(root, padding=10)\n",
    "    frame3.grid(row=5, column=1, sticky=W)\n",
    "    \n",
    "    button1 = ttk.Button(frame3, text=\"実行しちゃうお\", command=conductMain)\n",
    "    button1.pack(fill = \"x\", padx=30, side=\"left\")\n",
    "    \n",
    "    button2 = ttk.Button(frame3, text=(\"閉じちゃお\"), command=quit)\n",
    "    button2.pack(fill = \"x\", padx=30, side=\"left\")\n",
    "\n",
    "    \n",
    "    root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
