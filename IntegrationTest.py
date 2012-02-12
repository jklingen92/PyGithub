#!/bin/env python

from github import Github
import GithubCredentials

g = Github( GithubCredentials.login, GithubCredentials.password )

def dumpUser( u ):
    print u.login, "(", u.name, ")"
    print "  Repos:"
    for r in u.get_repos():
        print "   ", r.name,
        if r.fork:
            print "<-", r.parent.owner.login + "/" + r.parent.name,
            print "<-", r.source.owner.login + "/" + r.source.name,
        print
    print "  Watched:", ", ".join( r.name for r in u.get_watched() )
    print

def dumpOrganization( o ):
    print o.login, "(", o.name, ")"
    print "  Members:", ", ".join( u.login for u in o.get_members() )
    print

dumpUser( g.get_user() )
dumpUser( g.get_user( "nvie" ) )
dumpOrganization( g.get_organization( "github" ) )
dumpOrganization( g.get_organization( "BeaverSoftware" ) )