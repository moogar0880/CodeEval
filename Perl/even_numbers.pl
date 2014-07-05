#!/usr/bin/perl
use feature qw(say);
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

while(my $line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    if ($line % 2){
        say(0);
    }
    else{
        say(1);
    }
}
close(INFILE);