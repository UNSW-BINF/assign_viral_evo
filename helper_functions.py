def jukes_cantor(reference_sequence: str, distant_sequence: str) -> float:
    """The Jukes-Cantor correction for estimating genetic distances
    calculated with Hamming distance

    Parameters
    ----------
    referene_sequence: str
        A string of nucleotides in a sequence used as a reference
        in an alignment with other (i.e. ATGGC-TAG)
    distant_sequence: str
        A string of nucleotides in a sequence after the alignment
        with a reference (i.e. ATG-CTTAG)

    Returns
    -------
    float
        The Jukes-Cantor corrected genetic distance using Hamming distance.

    """
    raise NotImplementedError()


def kimura_two_parameter(reference_sequence: str, distant_sequence: str) -> float:
    """The Kimura Two Parameter correction for estimating genetic distances
    calculated with Hamming distance

    Parameters
    ----------
    referene_sequence: str
        A string of nucleotides in a sequence used as a reference
        in an alignment with other (i.e. ATGGC-TAG)
    distant_sequence: str
        A string of nucleotides in a sequence after the alignment
        with a reference (i.e. ATG-CTTAG)

    Returns
    -------
    float
        The Kimura corrected genetic distance using Hamming distance.

    """
    raise NotImplementedError()