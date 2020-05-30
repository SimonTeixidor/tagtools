#!/usr/bin/env python3 
import sys
import musicbrainzngs
musicbrainzngs.set_useragent("Simon's data fetcher", "0.1", "http://github.com/SimonPersson")

recording=musicbrainzngs.get_recording_by_id(
	sys.argv[1],
	includes=['artist-rels', 'instrument-rels', 'place-rels', 'area-rels']
)['recording']

def format_attribute(rel):
	return ', '.join(a['attribute'].split('(')[0].strip() for a in rel['attributes'])

def format_relation(rel):
	return f"PERFORMER={rel['artist']['name']} ({format_attribute(rel)})"

def format_single_place(place):
	if 'address' in place:
		return f"RECORDINGLOCATION={place['name']}, {place['address']}"
	return f"RECORDINGLOCATION={place['name']}"

def format_recording_place(recording):
	if 'place-relation-list' in recording:
		return [[
				format_single_place(place['place']),
				f"RECORDINGDATE={place['end']}" if 'end' in place else None
			] for place in recording['place-relation-list']
			if 'record' in place['type']]
	return []

def format_recording_location(recording):
	if 'area-relation-list' in recording:
		return [[
				f"RECORDINGLOCATION={place['area']['name']}",
				f"RECORDINGDATE={place['end']}" if 'end' in place else None
			] for place in recording['area-relation-list']
			if 'record' in place['type']]
	return []

if 'artist-relation-list' in recording:
	for relation in [r for r in recording['artist-relation-list'] if 'attributes' in r and r['type']=='instrument']:
		print(format_relation(relation))

	for relation in [r for r in recording['artist-relation-list'] if 'orchestra' in r['type']]:
		print(f"ENSEMBLE={relation['artist']['name']}")

	for relation in [r for r in recording['artist-relation-list'] if 'conductor' in r['type']]:
		print(f"CONDUCTOR={relation['artist']['name']}")

	for relation in [r for r in recording['artist-relation-list'] if 'recording' in r['type']]:
		print(f"ENGINEER={relation['artist']['name']}")

for p in (format_recording_place(recording) + format_recording_location(recording))[:1]:
	for l in p:
		if l != None:
			print(l)
