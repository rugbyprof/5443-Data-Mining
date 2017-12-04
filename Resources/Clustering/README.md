# Clustering Overview

### Clustering

- Clustering is an example of unsupervised learning
    - Number and form of classes {C<sub>i</sub>} unknown
    - Available data samples {x<sub>i</sub>} are unlabeled
    - Useful for discovery of data structure before classification or tuning or adaptation of classifiers
- Results strongly depend on the clustering algorithm

### Clustering Issues

- What defines a cluster?
    - Is there a prototype representing each cluster?
- What defines membership in a cluster?
    - What is the distance metric, d(x, y)?
- How many clusters are there?
    - Is the number of clusters picked before clustering?
- How well do the clusters represent unseen data?
    - How is a new data point assigned to a cluster?
    


### [K-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering)

k-means clustering is a method of vector quantization, originally from signal processing, that is popular for cluster analysis in data mining. k-means clustering aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells.

### [Hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering)

In data mining and statistics, hierarchical clustering (also called hierarchical cluster analysis or HCA) is a method of cluster analysis which seeks to build a hierarchy of clusters. Strategies for hierarchical clustering generally fall into two types:[1]

- **Agglomerative**: This is a "bottom up" approach: each observation starts in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.
- **Divisive**: This is a "top down" approach: all observations start in one cluster, and splits are performed recursively as one moves down the hierarchy.

### [DBScan](https://en.wikipedia.org/wiki/DBSCAN)

Density-based spatial clustering of applications with noise (DBSCAN) is a data clustering algorithm proposed by Martin Ester, Hans-Peter Kriegel, Jörg Sander and Xiaowei Xu in 1996.[1] It is a density-based clustering algorithm: given a set of points in some space, it groups together points that are closely packed together (points with many nearby neighbors), marking as outliers points that lie alone in low-density regions (whose nearest neighbors are too far away). DBSCAN is one of the most common clustering algorithms and also most cited in scientific literature.


### [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis)

- http://sebastianraschka.com/Articles/2014_pca_step_by_step.html

### iPython Notebooks

- [K-Means](K-Means-Clustering.ipynb)
- [DBScan](DBscan-Clustering.ipynb)
- [Hierarchical](Hierarchical-clustering.ipynb)
- [MST](MST-Clustering.ipynb)
- [Clustering MNIST Like Images](Clustering-Number-Images.ipynb)
- [Clustering Shapes](Clustering-Shapes.ipynb)

