#!/usr/bin/perl
use feature qw(say);
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

my $output;
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    $output = '';
    for my $word (split(' ', $line)){
        $output .= ' ';
        $output .= ucfirst($word);
    }
    say($output);
}
close(INFILE);