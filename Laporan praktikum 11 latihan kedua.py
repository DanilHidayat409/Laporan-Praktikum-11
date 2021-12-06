# -*- coding: utf-8 -*-
"""
@Hari/Tanggal : Senin,20211206
@Materi : Bublesort
@Judul : Laporan Praktikum 11
@NIM : 065002100032
@author: Muhammad Danil Hidayat
"""

class bubbleSort:
	

	def __init__(self, angka):
		self.angka = angka
		self.panjang = len(angka)

	def __str__(self):
		return " ".join([str(x)
						for x in self.angka])

	def bubbleSortRecursive(self, n = None):
		if n is None:
			n = self.panjang

		if n == 1:
			return

		for i in range(n - 1):
			if self.angka[i] > self.angka[i + 1]:
				self.angka[i], self.angka[i + 1] = self.angka[i + 1], self.angka[i]

		self.bubbleSortRecursive(n - 1)

def main():
	angka = [90, 34, 23, 1, 21, 43, 120,(-20)]
	
	
	sort = bubbleSort(angka)
	
	
	sort.bubbleSortRecursive()
	print("dengan sortingan sebagai berikut :\n", sort)


if __name__ == "__main__":
	main()
