using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace Clarans.Test
{
    public class ClaransTests
    {
        [Fact]
        public void DistanceTest()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 1, 1, 1 };

            Assert.Equal(0, cl.Distance(v1, v2));


            v1 = new List<double> { 1, 1, 1 };
            v2 = new List<double> { 2, 2, 2 };

            Assert.Equal(Math.Sqrt(3), cl.Distance(v1, v2));
        }

        [Fact]
        public void FindNearestTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };
            var m = new List<List<double>> { v1, v3 };
            var n1 = cl.FindNearestMedoid(m, v2);
            var n2 = cl.FindNearestMedoid(m, v4);

            Assert.Equal(v1, n1);
            Assert.Equal(v3, n2);
        }

        [Fact]
        public void ClusterizeTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };

            var medoids = new List<List<double>> { v1, v3 };
            var vectors = new List<List<double>> { v1, v2, v3, v4 };
            var clusters = cl.Clusterize(medoids, vectors);

            Assert.Equal(2, clusters.Keys.Count);
            Assert.Equal(2, clusters[v1].Count);
            Assert.Equal(2, clusters[v3].Count);
        }

        [Fact]
        public void ChooseMedoidsTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v = new List<List<double>> { v1, v2 };
            var m = cl.ChooseMedoids(v, 2);
            Assert.Equal(v, m.OrderBy(v => v[0]).ToList());
        }

        [Fact]
        public void ComputeCostTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };

            var medoids = new List<List<double>> { v1, v3 };
            var vectors = new List<List<double>> { v1, v2, v3, v4 };
            var clusters = cl.Clusterize(medoids, vectors);
            var cost = cl.ComputeCost(clusters);

            Assert.Equal(2 * Math.Sqrt(3), cost);
        }

        [Fact]
        public void ProcessTests()
        {
            var cl = new Clarans();
            var v1 = new List<double> { 1, 1, 1 };
            var v2 = new List<double> { 2, 2, 2 };
            var v3 = new List<double> { 8, 8, 8 };
            var v4 = new List<double> { 9, 9, 9 };
            var v = new List<List<double>> { v1, v2, v3, v4 };

            var clusters = cl.Process(v, 1, 10, 2);

            Assert.Equal(2, clusters.Count);
            // TODO: check medoids + items in cluster
        }
    }
}