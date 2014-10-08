import sys, time, traceback
import re, math

def get_cosine(item_vector1, item_vector2):
    intersection = set(item_vector1.keys()) & set(item_vector2.keys())
    numerator = sum([item_vector1[x] * item_vector2[x] for x in intersection])
    
    sum1 = sum([item_vector1[x]**2 for x in item_vector1.keys()])
    sum2 = sum([item_vector2[x]**2 for x in item_vector2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def get_sorensen_index(item_set1, item_set2):
    item_set1_len = len(item_set1)
    item_set2_len = len(item_set2)
    
    
    shared_set = item_set1.intersection(item_set2)
    shared_set_len = len(shared_set)
    
    if shared_set_len > 2 :
        qs = float((shared_set_len * 1.00) / (item_set1_len+item_set2_len))
        print "Sorensen index: %s - set_1 : %s - set_2: %s  - shared_set: %s"  % (qs, item_set1_len, item_set2_len, shared_set_len) 
    else:
        qs = 0
    
    return qs

def get_jaccard_index(item_set1, item_set2):
    shared_set = item_set1.intersection(item_set2)
    shared_set_len = len(shared_set)

    union_set = item_set1.union(item_set2)
    union_set_len = len(union_set)

    if shared_set_len > 2 :
            qs = shared_set_len * 1.00 / (union_set_len)
            print "Jackard index: %s - shared_set: %s - union_set: %s"  % (qs, shared_set_len, union_set_len) 
    else:
            qs = 0.00
    
    return qs

def get_morisita_index(vector_1, vector_2):
    
    vector_n = dict(vector_1, **vector_2)
    sum_1 = 0
    sum_2 = 0
    
    quadrat_1 = 0
    quadrat_2 = 0
    
    overlaps = 0
    
    for key,value in vector_n.items():
        value_1 = vector_1.get(key, 0)
        value_2 = vector_2.get(key, 0)
        
        overlaps += value_1*value_2

        quadrat_1 += value_1**2 
        quadrat_2 += value_2**2 

        sum_1 += value_1
        sum_2 += value_2
    
    horn_1 = quadrat_1*1.0/(sum_1**2)
    horn_2 = quadrat_2*1.0/(sum_2**2)
    index = 2.0 * overlaps/ ((horn_1+horn_2) *sum_1*sum_2+1)
    print "index: %s - overlaps: %s - horn_1: %s - horn_2: %s - sum_1: %s - sum_2: %s" % (index, overlaps, horn_1, horn_2, sum_1, sum_2)
    return index
