# https://info.cern.ch/hypertext/WWW/MarkUp/Connolly/MarkUp.html

Hypertext Markup Language

# HyperText Markup Language

## A Language for Transmission of Global Hyperdocuments.

### Abstract

The World Wide Web project involves the processing of structured
hypertext documents by diverse systems around the globe. The hypertext
documents are represented as marked up text.

## Specification

The HyperText Markup Language is defined in terms of the ISO
8879:1986, Standard Generalized Markup Language (SGML). The [SGML declaration and document type definition](https://cern.la/hypertext/WWW/MarkUp/Connolly/html.dtd)
specify the syntax and structure of HTML.

## Implementors' Guide

This is intended as an introduction to the language and a guide to
implementors. It does not comprise an integral part of the HTML
specification.

### Introduction

[Text and Markup](https://cern.la/hypertext/WWW/MarkUp/Connolly/Text.md) is an introduction to SGML
text and markup as it applies to HTML. It should prepare you to read
[the DTD](https://cern.la/hypertext/WWW/MarkUp/Connolly/html.dtd).

### HTML by Example

The following sections describe the HyperText Markup language by
example. They are organized in order of complexity, both for the human
reader and the SGML processing application.

[Recommended](https://cern.la/hypertext/WWW/MarkUp/Connolly/recommended.md): Examples of how to write HTML that won't stress the processing software. Some things can't be done this way. [Complete](https://cern.la/hypertext/WWW/MarkUp/Connolly/complete.md): Examples of all the constructs necessary to produce HTML documents. [Tolerated](https://cern.la/hypertext/WWW/MarkUp/Connolly/tolerated.md): Examples of illegal constructs that are supported for historical reasons. [Deprecated](https://cern.la/hypertext/WWW/MarkUp/Connolly/deprecated.md): Some quirks; these are legal SGML, but they are likely to break existing implementations (including the sample). [Errors](https://cern.la/hypertext/WWW/MarkUp/Connolly/errors.md): These are just plain broken. Implementors should use these to bullet-proof their code.

## A Partial Implementation

The [libHTML software
distribution](https://cern.la/hypertext/WWW/MarkUp/Connolly/libHTML.tar.Z) provides the primitive SGML reading functions that
you can use to build a conforming implementation.

This software is written in ANSI C (with some accomodataions for
K&R compilers). It supports the lexical constructs demonstrated in
[HTML Extremes](https://cern.la/hypertext/WWW/MarkUp/Connolly/supported.md).