#!/usr/bin/perl
use feature qw(say);
use File::stat;

open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

$stats = stat(INFILE);
say($stats->size);
close(INFILE);