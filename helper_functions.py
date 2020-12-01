from typing import Iterable, Dict, List


def kmers(seq: str, k: int, stride: int = 1) -> Iterable[str]:
    """Generate a list of k-mers from a given string.

    Parameters
    ----------
    seq: str
        A string which will be decomposed into k-mers.
    k: int
    stride: int

    Returns
    -------
    Iterable[str]

    """
    raise NotImplementedError()


def de_bruijn_graph(sequences: Iterable[str], k: int) -> Dict[str, List[str]]:
    """Construct a De Bruijn graph from a list of sequences.

    Given a list of strings, decompose each string into its respective k-mers
    (each string independently). When constructing k-mers, always use stride=1
    Then, construct the corresponding De Bruijn graph using all the k-mers
    produced in the first step. The De Bruijn graph should be given in edge-list
    format using a dictionary, where each dictionary entry corresponds to a node
    and its corresponding neighbors.

    For instance, given a string "abcde", you should return a graph
    corresponding to "abc" -> "bcd" -> "cde". If multiple strings are given with
    no overlap, your graph will contain disconnected components, e.g. for
    sequences "aaaa" and "bbbb", the graph should contain two disconnected
    components "aaa" -> "aaa" and "bbb" -> "bbb".

    Please use the tests to verify your implementation.

    Parameters
    ----------
    sequences: Iterable[str]
    k: int
        k for k-mers

    """
    raise NotImplementedError()


def assemble_genome(seqs: Iterable[str], k: int) -> List[str]:
    """Perform genome assembly using the Eulerian path algorithm.

    The overall algorithm should follow the following general structure:

    1. For an input list of sequences, construct a corresponding De Bruijn graph.
    2. Find all possible Euerlian paths through the graph, i.e. all possible paths
       which visit each edge exactly once. Your paths should all start from a
       source node with in-degree zero. In case no such node exists, you should
       start using the first k-mer of the first sequence in `seqs`. You can
       assume you will never encounter a disconnected graph.
    3. Decode your obtained paths into sequences, and return all unique genome
       assemblies.

    Parameters
    ----------
    seqs: List[str]
    k: int
        The k to be used to decompose the input strings into k-mers. The stride
        should always be set to 1.

    Returns
    -------
    List[str]
        A list of unique assemblies for the given `seqs`.

    """
    raise NotImplementedError()
