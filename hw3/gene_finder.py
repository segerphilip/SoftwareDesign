# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 4:06 2014

@author: Philip Seger
"""

from load import load_seq
dna = load_seq("./data/X73525.fa")
# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    #take dna and expand all values into a list 'sequence'
    sequence = list(dna)
    #then need to find length of list, which when divided by 3 tells us number of amino acids
    length = len(sequence)
    length = length / 3
    #eventually going to be used to store the AA pairs
    amino = []
    amino_acid_string = ''
    #using a for loop for going through each AA pair
    for b in range (length):
        #start and stop of codons
        start = 3 * b
        end = 3 * b + 3
        #amino is list of codons
        amino.append(dna[start:end])
        for index in range (len(codons)):
            #searches the list for the codon
            if amino[b] in codons[index]:
                #if found, adds proper aa to list
                amino_acid_string += (aa[index])
    return amino_acid_string


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    
    print 'input: ATGCCGATACTG, expected output: MPIL, actual: ' + coding_strand_to_AA('ATGCCGATACTG')    
    print 'input: CGGTAGGAACAA, expected output: R|EQ, actual: ' + coding_strand_to_AA('CGGTAGGAACAA')    
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    #empty string for eventual reverse sequence
    new_dna = ''
    #we want the reverse, so the while loop will count down
    i = len(dna) - 1
    while i >= 0:
        #if last one is A, changes to T and counts down one and then moves on
        if dna[i] == 'A':
            new_dna += ('T')
            i -= 1
        elif dna[i] == 'T':
            new_dna += ('A')
            i -= 1
        elif dna[i] == 'C':
            new_dna += ('G')
            i -= 1
        elif dna[i] == 'G':
            new_dna += ('C')
            i -= 1
    #return the resulting sequence
    return new_dna

    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print 'input: ATGCCGATACTG, expected output: CAGTATCGGCAT, actual: ' + get_reverse_complement('ATGCCGATACTG')    
    print 'input: CGGTAGGAACAA, expected output: TTGTTCCTACCG, actual: ' + get_reverse_complement('CGGTAGGAACAA')    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    #list for the codons
    codons = [None] * int(len(dna) / 3) 
    #empty list for open reading frames
    ORF = [] 
    for i in range(int(len(dna) / 3)):
        #reads in groups of 3
        codons[i] = dna[i * 3:i * 3 + 3] 
        #stops reading if it reaches the proper stop codons
        if codons[i] == 'TAG' or codons[i] == 'TAA' or codons[i] == 'TGA': 
            break
        else:
            ORF.append(codons[i])
    #creating a string output
    output_ORF = ''.join(ORF) 
    return output_ORF


def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    print 'input: ATGCTAATATGAA, expected output: ATGCTAATA, actual: ' + rest_of_ORF('ATGCTAATATGAA')    
    print 'input: ATGTTTTAG, expected output: ATGTTT, actual: ' + rest_of_ORF('ATGTTTTAG')
       

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    #create an empty list for use later
    orf_list = []
    i = 0 
    while i <= (len(dna)):
        #read only in groups of 3 for codons
        index = 3 * i 
        #start reading at ATG
        if dna[index:index + 3] == 'ATG': 
            string_of_orf = rest_of_ORF(dna[index:len(dna)]) 
            #throw sequence into orf_list
            orf_list.append(string_of_orf) 
            i = i + len(string_of_orf) / 3 
        else:
            #used if there is no ATG in group
            i += 1 
    
    return orf_list
     

def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print 'input: ACCTCAATGTTCCAGGTGTAAACCGAGGTCATGCAAAGATAA, expected output: ATGTTCCAGGTG, ATGCAAAGA, actual: ' + find_all_ORFs_oneframe('ACCTCAATGTTCCAGGTGTAAACCGAGGTCATGCAAAGATAA')


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
     
    #create an empty list for use later
    codon_group = [] 
    #loop through each frame, from 0 to 3
    for i in range(0,3): 
        codon_group += find_all_ORFs_oneframe(dna[i:]) 
    
    return codon_group


def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    print 'input: AATGCCGTGCCATAAGTTCAGATACCATAGGCTAAAATGAAATGGTCATGGATACCAAATAA, expected output: ATGAAATGGTCATGGATACCAAAT, ATGCCGTGCCATAAGTTCAGATACCATAGGCTAAAA, ATGGTCATGGATACCAAA, actual: ' + find_all_ORFs('AATGCCGTGCCATAAGTTCAGATACCATAGGCTAAAATGAAATGGTCATGGATACCAAATAA')


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    #empty lists for forward and back 
    codons_forward = [] 
    codons_backward = [] 
    #empty total list
    codons_complete = [] 
    #find first codons forward
    codons_forward += find_all_ORFs(dna)
    #find second codons backward 
    codons_backward += find_all_ORFs(get_reverse_complement(dna)) 
    #all the codons in one list
    all_the_codons = codons_forward + codons_backward 
    
    return all_the_codons


def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print 'input: ATGCCGATAGATCGACATGACATGAGATAC, expected output: ATGCCGATAGATCGACATGACATGAGATAC, ATGACA, ATGTCGATCTATCGGCAT, ATGTCATGTCGATCTATCGGC, actual: ' + find_all_ORFs_both_strands('ATGCCGATAGATCGACATGACATGAGATAC')


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    #set all_the_codons to all ORFs from before
    all_the_codons = find_all_ORFs_both_strands(dna) 
    #return an empty string if no ATG
    if not all_the_codons: 
        return '' 
    #sets start of longest codons as 0
    longest = all_the_codons[0] 
    #determines longer codons and replaces longest if longer than previous
    for i in range(1, len(all_the_codons)):
        if len(all_the_codons[i]) > len(longest):
            longest = all_the_codons[i] 
    
    return longest


def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    print 'input: ATACGACATAGTACATGCAATGCATGAAT, expected output: ATGCATTGCATGTACTATGTCGTA, actual: ' + longest_ORF('ATACGACATAGTACATGCAATGCATGAAT')

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    #need random numbers, so need random!
    import random
    output = 0
    #turn dna into a list and set to all_codons
    all_codons = list(dna) 
    for i in range(num_trials):
        #randomize the codons
        random.shuffle(all_codons) 
        #put lists into one
        random_dna = collapse(all_codons)
        longest = longest_ORF(random_dna) 
        if len(longest) > output:
            #if new is longer than old, replace old with new
            output = len(longest) 
    
    return output

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    #empty aa list
    complete_aa = []
    aa_list = find_all_ORFs_both_strands(dna) 
    for i in range(len(aa_list)):
        #add sequence if longer than threshold
        if len(aa_list[i]) >= threshold: 
            strand = aa_list[i]
            aa = coding_strand_to_AA(strand)
            #string added to list 
            complete_aa.append(aa) 
    
    return complete_aa
    
        
    #ran 1500 trials to find threshold, got 834, then 888, using 834
    #print longest_ORF_noncoding(dna,1500)
    #outputs aa
    #print gene_finder(dna,834) 
    #['MGDVSAVSSSGNILLPQQDEVGGLSEALKKAVEKHKTEYSGDKKDRDYGDAFVMHKETALPLLLAAWRHGAPAKSEHHNGNVSGLHHNGKSELRIAEKLLKVTAEKSVGLISAEAKVDKSAALLSSKNRPLESVSGKKLSADLKAVESVSEVTDNATGISDDNIKALPGDNKAIAGEGVRKEGAPLARDVAPARMAAANTGKPEDKDHKKVKDVSQLPLQPTTIADLSQLTGGDEKMPLAAQSKPMMTIFPTADGVKGEDSSLTYRFQRWGNDYSVNIQARQAGEFSLIPSNTQVEHRLHDQWQNGNPQRWHLTRDDQQNPQQQQHRQQSGEEDDA',
    # 'MSLRVRQIDRREWLLAQTATECQRHGREATLEYPTRQGMWVRLSDAEKRWSAWIKPGDWLEHVSPALAGAAVSAGAEHLVVPWLAATERPFELPVPHLSCRRLCVENPVPGSALPEGKLLHIMSDRGGLWFEHLPELPAVGGGRPKMLRWPLRFVIGSSDTQRSLLGRIGIGDVLLIRTSRAEVYCYAKKLGHFNRVEGGIIVETLDIQHIEEENNTTETAETLPGLNQLPVKLEFVLYRKNVTLAELEAMGQQQLLSLPTNAELNVEIMANGVLLGNGELVQMNDTLGVEIHEWLSESGNGE', 
    # 'MSSNKTEKPTKKRLEDSAKKGQSFKSKDLIIACLTLGGIAYLVSYGSFNEFMGIIKIIIADNFDQSMADYSLAVFGIGLKYLIPFMLLCLVCSALPALLQAGFVLATEALKPNLSALNPVEGAKKLFSMRTVKDTVKTLLYLSSFVVAAIICWKKYKVEIFSQLNGNIVGIAVIWRELLLALVLTCLACALIVLLLDAIAEYFLTMKDMKMDKEEVKREMKEQEGNPEVKSKRREVHMEILSEQVKSDIENSRLIVANPTHITIGIYFKPELMPIPMISVYETNQRALAVRAYAEKVGVPVIVDIKLARSLFKTHRRYDLVSLEEIDEVLRLLVWLEEVENAGKDVIQPQENEVRH']