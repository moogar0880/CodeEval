#!/usr/bin/perl
use feature qw(say);
open(INFILE, "<$ARGV[0]") or die("Cannot open file $ARGV[0] for reading: $!");

my $output;
while(my $line = <INFILE>) {
    next if($line =~ m/^s$/);
    $line =~ s/(^s|s*$)//g;
    $output = '';
    my($a, $b, $n) = split(' ', $line);

    for $i (1..$n){
        if (!($i % $a) and !($i % $b)){
            $output .= 'FB';
        }
        elsif (!($i % $a)){
            $output .= 'F';
        }
        elsif (!($i % $b)){
            $output .= 'B';
        }
        else{
            $output .= $i;
        }
        $output .= ' ';
    }

    say(substr $output, 0, -1);
}
close(INFILE);