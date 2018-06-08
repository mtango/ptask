#! /usr/bin/env python
# encoding: utf-8

APPNAME='ptask'

top = '.'
out = 'build'

def options(ctx):
    ctx.load('compiler_c')
    ctx.add_option('--with-tests', action='store_true', default=False, help='Build tests')
    ctx.add_option('--with-examples', action='store_true', default=False, help='Build examples')

def configure(ctx):
    ctx.load('compiler_c')
    print('Building with tests: {}'.format(ctx.options.with_tests))
    print('Building with examples: {}'.format(ctx.options.with_examples))
    if ctx.options.with_examples:
        ctx.recurse('examples')

def build(ctx):
    ctx.recurse('src')

    if ctx.options.with_examples:
        ctx.recurse('examples')
    if ctx.options.with_tests:
        ctx.recurse('tests')

