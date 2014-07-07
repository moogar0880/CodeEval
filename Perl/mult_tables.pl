#!/usr/bin/perl
use feature qw(say);

sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

my $output;
my $cell = '    ';

for $i (1..12){
    $output = '';
    for $j (1..12){
        $output .= substr $cell, 0, -(length($i * $j));
        $output .= $i * $j;
    }
    say(trim($output));
}