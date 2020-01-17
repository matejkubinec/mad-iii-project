using System;
using System.Collections.Generic;
using System.Linq;

namespace Clarans
{
    public class Clarans
    {
        private Random _random = new Random();

        /// <summary>
        /// Computes CLARANS clustering algorithm on supplied data.
        /// </summary>List
        /// <param name="data">Data to be clustered.</param>
        /// <param name="maxNeighbours">The maximum number of neighbours examined.</param>
        /// <param name="numLocal">Amount of iterations for solving the problem.</param>
        /// <param name="k">Number of clusters.</param>
        public Dictionary<List<double>, List<List<double>>> Process(List<List<double>> data, int maxNeighbours, int numLocal, int k)
        {
            if (data.Count < 0)
            {
                throw new ArgumentException("Argument 'data' cannot be of length 0.");
            }

            if (maxNeighbours < 0)
            {
                throw new ArgumentException("Argument 'maxNeighbours' must be greater than 0.");
            }

            if (numLocal < 0)
            {
                throw new ArgumentException("Argument 'numLocal' must be greater than 0.");
            }

            var minCost = double.PositiveInfinity;
            var bestNode = new Dictionary<List<double>, List<List<double>>>();

            for (var i = 0; i < numLocal; i++)
            {
                var medoids = ChooseMedoids(data, k);
                var clusters = Clusterize(medoids, data);

                var j = 0;
                while (j < maxNeighbours)
                {
                    var medoid = PickRandom(medoids);
                    var neighbour = PickRandom(clusters[medoid]);
                    var previousCost = ComputeCost(clusters);

                    if (medoid == neighbour)
                    {
                        continue;
                    }

                    clusters[neighbour] = clusters[medoid];
                    clusters.Remove(medoid);

                    var cost = ComputeCost(clusters);

                    if (cost <= previousCost)
                    {
                        medoids.Remove(medoid);
                        medoids.Add(neighbour);
                        j++;
                    }
                    else
                    {
                        if (!clusters.ContainsKey(medoid))
                        {
                            clusters.Add(medoid, clusters[neighbour]);
                        }
                        else
                        {
                            clusters[medoid] = clusters[neighbour];
                        }

                        clusters.Remove(neighbour);
                    }
                }


                var totalCost = ComputeCost(clusters);

                if (totalCost < minCost)
                {
                    bestNode = clusters;
                }
            }

            return bestNode;
        }

        public double ComputeCost(Dictionary<List<double>, List<List<double>>> clusters)
        {
            var cost = 0.0;
            foreach (var medoid in clusters.Keys)
            {
                foreach (var item in clusters[medoid])
                {
                    cost += Distance(medoid, item);
                }
            }
            return cost;
        }

        public List<double> PickRandom(List<List<double>> v)
        {
            var idx = _random.Next(0, v.Count);
            return v[idx];
        }

        public List<List<double>> ChooseMedoids(List<List<double>> data, int numLocal)
        {
            var samples = new List<List<double>>();

            while (samples.Count < numLocal)
            {
                var idx = _random.Next(0, data.Count);
                var item = data[idx];

                if (samples.Contains(item))
                {
                    continue;
                }

                samples.Add(item);
            }

            return samples;
        }

        public Dictionary<List<double>, List<List<double>>> Clusterize(List<List<double>> medoids, List<List<double>> data)
        {
            var clusters = new Dictionary<List<double>, List<List<double>>>();

            foreach (var item in data)
            {
                var nearest = FindNearestMedoid(medoids, item);

                if (clusters.ContainsKey(nearest))
                {
                    clusters[nearest].Add(item);
                }
                else
                {
                    clusters[nearest] = new List<List<double>> { item };
                }
            }

            return clusters;
        }

        public List<double> FindNearestMedoid(List<List<double>> medoids, List<double> item)
        {
            var minDistance = double.PositiveInfinity;
            var nearest = medoids.First();

            foreach (var medoid in medoids)
            {
                var distance = Distance(medoid, item);

                if (distance < minDistance)
                {
                    nearest = medoid;
                    minDistance = distance;
                }
            }

            return nearest;
        }

        public double Distance(List<double> v1, List<double> v2)
        {
            var sum = 0.0;
            for (var i = 0; i < v1.Count; i++)
            {
                sum += Math.Pow(v1[i] - v2[i], 2);
            }
            return Math.Sqrt(sum);
        }
    }
}
