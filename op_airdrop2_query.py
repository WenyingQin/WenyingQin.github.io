import csv

def read_address_txt(file_path):
    with open(file_path, 'r') as f:
        addresses = [line.strip().lower() for line in f.readlines()]
    return addresses

def read_score_csv(file_path):
    scores = {}
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            address, score = row
            scores[address.lower()] = score
    return scores

def query_scores(addresses, scores):
    results = {}
    for address in addresses:
        if address in scores:
            results[address] = scores[address]
        else:
            results[address] = None
    return results

def write_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for address, score in results.items():
            writer.writerow([address, score])

def main():
    addresses = read_address_txt('address.txt')
    scores = read_score_csv('score.csv')
    results = query_scores(addresses, scores)
    write_results_to_csv(results, 'results.csv')

if __name__ == '__main__':
    main()

