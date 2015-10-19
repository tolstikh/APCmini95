# -*- coding: utf-8 -*-
# flake8: noqa

# // APC Colors for 5x8 clip matrix
# var APC_COLOR_BLACK        = 0;   // off, 
# var APC_COLOR_GREEN        = 1;   // green, 7-127 also green
# var APC_COLOR_GREEN_BLINK  = 2;   // green blink, 
# var APC_COLOR_RED          = 3;   // red, 
# var APC_COLOR_RED_BLINK    = 4;   // red blink, 
# var APC_COLOR_YELLOW       = 5;   // yellow, 
# var APC_COLOR_YELLOW_BLINK = 6;   // yellow blink,

# APCmini colours
LED_OFF = 0

GREEN_FULL = 1
GREEN_HALF = 1
GREEN_THIRD = 1
GREEN_BLINK = 2

RED_FULL = 3
RED_HALF = 3
RED_THIRD = 3
RED_BLINK = 4

AMBER_FULL = 5
AMBER_HALF = 5
AMBER_THIRD = 5
AMBER_BLINK = 6

# Scales
KEY_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
CIRCLE_OF_FIFTHS = [7 * k % 12 for k in range(12)]
# KEY_CENTERS = CIRCLE_OF_FIFTHS[0:6] + CIRCLE_OF_FIFTHS[-1:5:-1]

MUSICAL_MODES = [

	'Major',			[0, 2, 4, 5, 7, 9, 11],
	'Minor',			[0, 2, 3, 5, 7, 8, 10],
	'Dorian',			[0, 2, 3, 5, 7, 9, 10],
	'Mixolydian',		[0, 2, 4, 5, 7, 9, 10],
	'Lydian',			[0, 2, 4, 6, 7, 9, 11],
	'Phrygian',			[0, 1, 3, 5, 7, 8, 10],
	'Locrian',			[0, 1, 3, 5, 6, 8, 10],
	'Diminished',		[0, 1, 3, 4, 6, 7, 9, 10],

	'Whole-half',		[0, 2, 3, 5, 6, 8, 9, 11],
	'Whole Tone',		[0, 2, 4, 6, 8, 10],
	'Minor Blues',		[0, 3, 5, 6, 7, 10],
	'Minor Pentatonic', [0, 3, 5, 7, 10],
	'Major Pentatonic', [0, 2, 4, 7, 9],
	'Harmonic Minor',	[0, 2, 3, 5, 7, 8, 11],
	'Melodic Minor',	[0, 2, 3, 5, 7, 9, 11],
	'Super Locrian',	[0, 1, 3, 4, 6, 8, 10],

	'Bhairav',			[0, 1, 4, 5, 7, 8, 11],
	'Hungarian Minor',	[0, 2, 3, 6, 7, 8, 11],
	'Minor Gypsy',		[0, 1, 4, 5, 7, 8, 10],
	'Hirojoshi',		[0, 2, 3, 7, 8],
	'In-Sen',			[0, 1, 5, 7, 10],
	'Iwato',			[0, 1, 5, 6, 10],
	'Kumoi',			[0, 2, 3, 7, 9],
	'Pelog',			[0, 1, 3, 4, 7, 8],

	'Spanish',			[0, 1, 3, 4, 5, 6, 8, 10],
	'IonEol',			[0, 2, 3, 4, 5, 7, 8, 9, 10, 11]  # from aschneiderg@unal.edu.co
]


def index_of(list, elt):
	for i in range(0, len(list)):
		if (list[i] == elt):
			return i
	return(-1)
