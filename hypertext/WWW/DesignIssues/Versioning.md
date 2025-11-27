HyperText Design Issues: Versioning

# Versioning

Definition: The storage and management of previous copies of a piece
of information, for security, diagnostics, and interest.

Do you want version control?

Can you reference a version only?

If you refer to a particular place in a node, how does one follow
it in a new version, if that place ceases to exist?

(ˆPeter Aiken is the expert in this area¤ - Tim Oren, Apple)

Yes, at CERN we will want versioning. Very often one wants to correct
a news item, even one of limited life, without reissuing it. This
is a problem with VAX/NOTES for example. I would suggest that the
text for the current version is stored, and separately those modifications
necessary to backtrack to previous versions. I would expect previous
versions to be regenerated only on the fly, as needed. (Apparaently
SCCS stores the original file and the differences. This system does
allow you to ditsribute the differences when updating copies.)

If full differences (deltas) are kept, the first version is just the
first delta from a null document. The latest version is not available
without regenerating it from all the deltas. For speed, it is obviously
useful to keep a copy of the latest version (see [caching](https://cern.la/hypertext/WWW/DesignIssues/Caching.md) ).

Versioning is necessary for accountability (--David Durand, dgd@cs.bu.edu).
If an author is to be accountable for information published, it should
be possible to demonstrate later what he wrote, even if he has later
changed it.

A WWW server may provide versioning, by allowing links between a document
version and its previou and succesive versions. This would be a good
use of [link typing](https://cern.la/hypertext/WWW/DesignIssues/LinkTypes.md#1) .

Keeping track of versions allows one solution to the [annotation problem](https://cern.la/hypertext/WWW/DesignIssues/Annotation.md).