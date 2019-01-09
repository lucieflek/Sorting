import random
import time
import numpy as np
import scipy.optimize as opt;
import matplotlib.pyplot as plt

# GLOBALE PARAMETER
UNSORTED 			= 1
PARTIALLY_SORTED 	= 2
NOPLOT				= 0
PLOT				= 1
PLOT_WITHFIT		= 2

# Globale Variablen (sicher haeslsich, aber hier ausreichend :) )
mBaseRandomList 		= []
mBaseRandomSortedList 	= []

# Returns the value of a parabola with the parameters a,b,c
def parabola(x, a, b, c):
	return a*x**2 + b*x + c

# Returns the value of a n*log(n) function with the parameters a,b
def nlogn(x, a):
	return a*x*np.log(x)

# Returns a List of length "size" filled with random numbers between 0.1
def initializeRandomNumberList():
	global mBaseRandomList
	global mBaseRandomSortedList
	print "Initialize Random Number List...",
	mBaseRandomList = [int(random.uniform(0, 500000)) for i in 500000 * [None]]
	for i in range(0, 500000): 
		mBaseRandomSortedList.append(i+50+int(random.uniform(-50, 50)))
	print "done"

# Returns a List of length "size" filled with random numbers between 0.1
def makeRandomNumberList(size, isPartlySorted=UNSORTED):
	global mBaseRandomList
	global mBaseRandomSortedList
	if isPartlySorted==UNSORTED:
		return mBaseRandomList[0:size]
	if isPartlySorted==PARTIALLY_SORTED:
		return mBaseRandomSortedList[0:size]

# Draw x- and y-values and fits a 2nd order polynomial
def plotPerformanceResults(xList, yList, FigureTitle, plotResults=PLOT):
	# Setting up the figure
	fig = plt.figure()
	fig.patch.set_facecolor('white')
	ax = fig.add_subplot(111)
	plt.xlabel('Length of List', fontsize=18)
	plt.ylabel('Time [s]', fontsize=18)
	# Plotting the values
	plt.plot(xList, yList, label='Messpunkte', color='orange', linestyle='', marker='o', markersize=10)
	# Fitting with a Polynomial
	fit_params_p2, pcov_p2 = opt.curve_fit(parabola, np.asarray(xList), np.asarray(yList))
	fit_params_nl, pcov_nl = opt.curve_fit(nlogn, np.asarray(xList), np.asarray(yList))
	x_fit	= list(range(int(xList[0]), int(xList[-1])))
	y_fit_p2= parabola(np.asarray(x_fit), *fit_params_p2)
	y_fit_nl= nlogn(np.asarray(x_fit), *fit_params_nl)
	# Plotting the fitted Line
	if plotResults==PLOT_WITHFIT:
		plt.plot(np.asarray(x_fit), y_fit_p2, label='Polynom 2te Ordnung (Fit)', color='dodgerblue', linewidth=2.0) 
		#plt.plot(np.asarray(x_fit), y_fit_nl, label='n*log(n) (Fit)', color='darkviolet', linestyle='--', linewidth=2.0) 
	# Add Legend and Text
	plt.legend(loc='upper left', frameon=False)
	plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.1)
	plt.text(0.025, 0.72, "Sortieralgorithmus: "+FigureTitle, fontsize=14, transform = ax.transAxes)
	plt.text(0.025, 0.65, "(L. Flekova 2018)", fontsize=14, transform = ax.transAxes)
	# Show the result
	fig.savefig(FigureTitle+".png")
	plt.show()

# Funktion welche die Laenge der Eingangsdaten ermittelt, so dass die Sortierung mehr als 0.01s benoetigt
def findOptimalStatistics(funktion, nUseUnSortedList=UNSORTED):
	print "Determining reasonable statistics for "+funktion.func_name+"...",
	for i in [1,2,4,8,12,24,36,50]:
		liste = makeRandomNumberList(200*i, nUseUnSortedList)
		startTime = time.time()
		funktion(liste)
		endeTime = time.time()
		dTime = float('{:5.3f}'.format(endeTime-startTime))
		if dTime>0.02:
			print "done"
			return 100*i
	print "done"
	return 100*i

# Funktion welche die Sortierung fuer 10 unterschiedlich Lange Listen
# durchfuehrt. 
# @funktion = Funktion zum Sortieren, die getestet werden soll
def performanceStudy(funktion, plotResults=NOPLOT, nUseUnSortedList=UNSORTED):
	# Bestimme Laenge der Liste, fuer die unser Algorithmus etwa 0.01s zum sortieren benoetigt
	lengthOfList = findOptimalStatistics(funktion, nUseUnSortedList)
	listStepSize	= [1,2,3,4,5,6,7,8,9]
	xListLength	= []
	yTime		= []
	# Schleife fuer 10 Sortierungen von Listen unterschiedlicher Laenge
	for i in listStepSize:
		# Erzeugung der Liste mit lengthOfList*i Elementen
		liste = makeRandomNumberList(lengthOfList*i, nUseUnSortedList)
		startTime = time.time()
		# Sortierung
		funktion(liste)
		endeTime = time.time()
		# Ausgabe der benoetigten Zeit 
		print "Laenge der Liste: ",lengthOfList*i,"Elemente	   Benoetige Zeit zum Sortieren:", '{:5.3f}s'.format(endeTime-startTime)
		# Ergebnisse werden gespeichert
		xListLength.append(float(lengthOfList*i))
		yTime.append(float('{:5.3f}'.format(endeTime-startTime)))
	# Ergebisse werden geplottet
	if plotResults!=NOPLOT:
		plotPerformanceResults(xListLength, yTime, funktion.func_name, plotResults)

