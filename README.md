**[JQpy](https://pypi.org/project/jqpy/)** is Python binding for [JQ](https://jqlang.github.io/jq/) (JSON processing language) that simply works on any platform (even Windows) and does not require compilation.

[Read the documentation](https://baterflyrity.github.io/jqpy/)

----

<!-- TOC -->
* [Tutorial](#tutorial)
* [Installation](#installation)
<!-- TOC -->

# Tutorial

GitHub has a JSON API, so let's play with that. This URL gets us the last 5 commits from the jq repo.

```ipython
>>> import requests
>>> data = requests.get('https://api.github.com/repos/jqlang/jq/commits',{'per_page':5}).json()
>>> data
```

<details>
  	<summary>Show result</summary>

	[
		{
			'sha': 'bfb7fd570f521ef832fe1c3bca0e05abd398284c',
			'node_id': 
	'C_kwDOAE3WVdoAKGJmYjdmZDU3MGY1MjFlZjgzMmZlMWMzYmNhMGUwNWFiZDM5ODI4NGM',
			'commit': {
				'author': {
					'name': 'David Korczynski',
					'email': 'david@adalogics.com',
					'date': '2023-11-30T13:33:01Z'
				},
				'committer': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-30T13:40:36Z'
				},
				'message': 'jq_fuzz_execute: cleanup un-needed 
	extern\n\nSigned-off-by: David Korczynski <david@adalogics.com>',
				'tree': {
					'sha': '47b08e6bc3e47c9ab13092d613bda7e4cf35bba0',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/47b08e6bc3e47c9ab13092d613bda
	7e4cf35bba0'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/bfb7fd570f521ef832fe1c3bca0
	e05abd398284c',
				'comment_count': 0,
				'verification': {
					'verified': False,
					'reason': 'unsigned',
					'signature': None,
					'payload': None
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/bfb7fd570f521ef832fe1c3bca0e05a
	bd398284c',
			'html_url': 
	'https://github.com/jqlang/jq/commit/bfb7fd570f521ef832fe1c3bca0e05abd398284c',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/bfb7fd570f521ef832fe1c3bca0e05a
	bd398284c/comments',
			'author': {
				'login': 'DavidKorczynski',
				'id': 657617,
				'node_id': 'MDQ6VXNlcjY1NzYxNw==',
				'avatar_url': 'https://avatars.githubusercontent.com/u/657617?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/DavidKorczynski',
				'html_url': 'https://github.com/DavidKorczynski',
				'followers_url': 
	'https://api.github.com/users/DavidKorczynski/followers',
				'following_url': 
	'https://api.github.com/users/DavidKorczynski/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/DavidKorczynski/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/DavidKorczynski/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/DavidKorczynski/subscriptions',
				'organizations_url': 
	'https://api.github.com/users/DavidKorczynski/orgs',
				'repos_url': 'https://api.github.com/users/DavidKorczynski/repos',
				'events_url': 
	'https://api.github.com/users/DavidKorczynski/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/DavidKorczynski/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': '252ab244cead3670a11d06bc3110f3a4577a2341',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/252ab244cead3670a11d06bc3110f3a
	4577a2341',
					'html_url': 
	'https://github.com/jqlang/jq/commit/252ab244cead3670a11d06bc3110f3a4577a2341'
				}
			]
		},
		{
			'sha': '252ab244cead3670a11d06bc3110f3a4577a2341',
			'node_id': 
	'C_kwDOAE3WVdoAKDI1MmFiMjQ0Y2VhZDM2NzBhMTFkMDZiYzMxMTBmM2E0NTc3YTIzNDE',
			'commit': {
				'author': {
					'name': 'David Korczynski',
					'email': 'david@adalogics.com',
					'date': '2023-11-30T13:22:27Z'
				},
				'committer': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-30T13:40:36Z'
				},
				'message': 'Add fuzzer targeting jq_next\n\nSigned-off-by: David 
	Korczynski <david@adalogics.com>',
				'tree': {
					'sha': '7c6832a4b7376e7793d1239bd0abe0d580c69ee3',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/7c6832a4b7376e7793d1239bd0abe
	0d580c69ee3'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/252ab244cead3670a11d06bc311
	0f3a4577a2341',
				'comment_count': 0,
				'verification': {
					'verified': False,
					'reason': 'unsigned',
					'signature': None,
					'payload': None
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/252ab244cead3670a11d06bc3110f3a
	4577a2341',
			'html_url': 
	'https://github.com/jqlang/jq/commit/252ab244cead3670a11d06bc3110f3a4577a2341',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/252ab244cead3670a11d06bc3110f3a
	4577a2341/comments',
			'author': {
				'login': 'DavidKorczynski',
				'id': 657617,
				'node_id': 'MDQ6VXNlcjY1NzYxNw==',
				'avatar_url': 'https://avatars.githubusercontent.com/u/657617?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/DavidKorczynski',
				'html_url': 'https://github.com/DavidKorczynski',
				'followers_url': 
	'https://api.github.com/users/DavidKorczynski/followers',
				'following_url': 
	'https://api.github.com/users/DavidKorczynski/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/DavidKorczynski/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/DavidKorczynski/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/DavidKorczynski/subscriptions',
				'organizations_url': 
	'https://api.github.com/users/DavidKorczynski/orgs',
				'repos_url': 'https://api.github.com/users/DavidKorczynski/repos',
				'events_url': 
	'https://api.github.com/users/DavidKorczynski/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/DavidKorczynski/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': '13353515bd3aedf84c6e6ebfb726563ae84db778',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/13353515bd3aedf84c6e6ebfb726563
	ae84db778',
					'html_url': 
	'https://github.com/jqlang/jq/commit/13353515bd3aedf84c6e6ebfb726563ae84db778'
				}
			]
		},
		{
			'sha': '13353515bd3aedf84c6e6ebfb726563ae84db778',
			'node_id': 
	'C_kwDOAE3WVdoAKDEzMzUzNTE1YmQzYWVkZjg0YzZlNmViZmI3MjY1NjNhZTg0ZGI3Nzg',
			'commit': {
				'author': {
					'name': 'David Korczynski',
					'email': 'david@adalogics.com',
					'date': '2023-11-30T13:22:07Z'
				},
				'committer': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-30T13:40:36Z'
				},
				'message': 'jq_fuzz_compile: dump disassembly\n\nSigned-off-by: 
	David Korczynski <david@adalogics.com>',
				'tree': {
					'sha': 'a4fe1a9f424352a5f989b629ba666ccacd3ebd61',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/a4fe1a9f424352a5f989b629ba666
	ccacd3ebd61'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/13353515bd3aedf84c6e6ebfb72
	6563ae84db778',
				'comment_count': 0,
				'verification': {
					'verified': False,
					'reason': 'unsigned',
					'signature': None,
					'payload': None
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/13353515bd3aedf84c6e6ebfb726563
	ae84db778',
			'html_url': 
	'https://github.com/jqlang/jq/commit/13353515bd3aedf84c6e6ebfb726563ae84db778',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/13353515bd3aedf84c6e6ebfb726563
	ae84db778/comments',
			'author': {
				'login': 'DavidKorczynski',
				'id': 657617,
				'node_id': 'MDQ6VXNlcjY1NzYxNw==',
				'avatar_url': 'https://avatars.githubusercontent.com/u/657617?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/DavidKorczynski',
				'html_url': 'https://github.com/DavidKorczynski',
				'followers_url': 
	'https://api.github.com/users/DavidKorczynski/followers',
				'following_url': 
	'https://api.github.com/users/DavidKorczynski/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/DavidKorczynski/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/DavidKorczynski/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/DavidKorczynski/subscriptions',
				'organizations_url': 
	'https://api.github.com/users/DavidKorczynski/orgs',
				'repos_url': 'https://api.github.com/users/DavidKorczynski/repos',
				'events_url': 
	'https://api.github.com/users/DavidKorczynski/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/DavidKorczynski/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': '98a206964d59143c6ed9189b91cdb34af1ae5071',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/98a206964d59143c6ed9189b91cdb34
	af1ae5071',
					'html_url': 
	'https://github.com/jqlang/jq/commit/98a206964d59143c6ed9189b91cdb34af1ae5071'
				}
			]
		},
		{
			'sha': '98a206964d59143c6ed9189b91cdb34af1ae5071',
			'node_id': 
	'C_kwDOAE3WVdoAKDk4YTIwNjk2NGQ1OTE0M2M2ZWQ5MTg5YjkxY2RiMzRhZjFhZTUwNzE',
			'commit': {
				'author': {
					'name': 'Mattias Wadman',
					'email': 'mattias.wadman@gmail.com',
					'date': '2023-11-29T08:36:33Z'
				},
				'committer': {
					'name': 'GitHub',
					'email': 'noreply@github.com',
					'date': '2023-11-29T08:36:33Z'
				},
				'message': 'Convert decnum to binary64 (double) instead of 
	decimal64\n\nThis is what the JSON spec suggests and will also be less 
	confusing compared to other jq implementations and langauges.\r\n\r\nRelated to
	#2939',
				'tree': {
					'sha': 'e8055db585b3fa602b289b1fc2e725e293600a17',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/e8055db585b3fa602b289b1fc2e72
	5e293600a17'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/98a206964d59143c6ed9189b91c
	db34af1ae5071',
				'comment_count': 0,
				'verification': {
					'verified': True,
					'reason': 'valid',
					'signature': '-----BEGIN PGP 
	SIGNATURE-----\n\nwsBcBAABCAAQBQJlZvgRCRBK7hj4Ov3rIwAAe+MIAB0NJnboF3tHVY+d6VqlY
	Fxe\nA4RP/9ZjFlUrRLCe5jwQU9irhDQuPICjvYa/K0xrIc3oaAnTE4AEM7HxJku9sGdj\ngfRZI1BV
	XKMTpGz0cWX7HpDCJsz9oGIR4myNXyJdsHSgaMeE8/QnedGt2PTGyFoV\nAdH6bj8XyirrPEvJtnhlo
	NS7GMrTfWjVIBRhP5OqIsSN4MgRbxGBHdLTB+g+V/Vq\nRHji3DUdD6HyWrdmwJ3zAlMkyjcfvtgkyY
	OHj9qYWFNXDWtfB1nlhbqW+MVGScOD\nOkZguRVV3xgRa6EFjn32ltzcwB1B5XsoQF+PWfX1pfEseEO
	HVyTFdo/kufADLQM=\n=fC+V\n-----END PGP SIGNATURE-----\n',
					'payload': 'tree 
	e8055db585b3fa602b289b1fc2e725e293600a17\nparent 
	16170910332b51f1ff497ef566d6a525acdb5b43\nauthor Mattias Wadman 
	<mattias.wadman@gmail.com> 1701246993 +0100\ncommitter GitHub 
	<noreply@github.com> 1701246993 +0100\n\nConvert decnum to binary64 (double) 
	instead of decimal64\n\nThis is what the JSON spec suggests and will also be 
	less confusing compared to other jq implementations and 
	langauges.\r\n\r\nRelated to #2939'
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/98a206964d59143c6ed9189b91cdb34
	af1ae5071',
			'html_url': 
	'https://github.com/jqlang/jq/commit/98a206964d59143c6ed9189b91cdb34af1ae5071',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/98a206964d59143c6ed9189b91cdb34
	af1ae5071/comments',
			'author': {
				'login': 'wader',
				'id': 185566,
				'node_id': 'MDQ6VXNlcjE4NTU2Ng==',
				'avatar_url': 'https://avatars.githubusercontent.com/u/185566?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/wader',
				'html_url': 'https://github.com/wader',
				'followers_url': 'https://api.github.com/users/wader/followers',
				'following_url': 
	'https://api.github.com/users/wader/following{/other_user}',
				'gists_url': 'https://api.github.com/users/wader/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/wader/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/wader/subscriptions',
				'organizations_url': 'https://api.github.com/users/wader/orgs',
				'repos_url': 'https://api.github.com/users/wader/repos',
				'events_url': 
	'https://api.github.com/users/wader/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/wader/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'web-flow',
				'id': 19864447,
				'node_id': 'MDQ6VXNlcjE5ODY0NDQ3',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/19864447?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/web-flow',
				'html_url': 'https://github.com/web-flow',
				'followers_url': 'https://api.github.com/users/web-flow/followers',
				'following_url': 
	'https://api.github.com/users/web-flow/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/web-flow/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/web-flow/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/web-flow/subscriptions',
				'organizations_url': 'https://api.github.com/users/web-flow/orgs',
				'repos_url': 'https://api.github.com/users/web-flow/repos',
				'events_url': 
	'https://api.github.com/users/web-flow/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/web-flow/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': '16170910332b51f1ff497ef566d6a525acdb5b43',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/16170910332b51f1ff497ef566d6a52
	5acdb5b43',
					'html_url': 
	'https://github.com/jqlang/jq/commit/16170910332b51f1ff497ef566d6a525acdb5b43'
				}
			]
		},
		{
			'sha': '16170910332b51f1ff497ef566d6a525acdb5b43',
			'node_id': 
	'C_kwDOAE3WVdoAKDE2MTcwOTEwMzMyYjUxZjFmZjQ5N2VmNTY2ZDZhNTI1YWNkYjViNDM',
			'commit': {
				'author': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-29T05:12:25Z'
				},
				'committer': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-29T08:35:36Z'
				},
				'message': 'website: use https URLs instead of http URLs in 
	download page\n\nAlso add markdown formatting for decNumber URL so it gets 
	rendered as a\nlink in the html page.',
				'tree': {
					'sha': 'ff8b801f14994e4a177ee22b3c9b649281ec8af6',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/ff8b801f14994e4a177ee22b3c9b6
	49281ec8af6'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/16170910332b51f1ff497ef566d
	6a525acdb5b43',
				'comment_count': 0,
				'verification': {
					'verified': False,
					'reason': 'unsigned',
					'signature': None,
					'payload': None
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/16170910332b51f1ff497ef566d6a52
	5acdb5b43',
			'html_url': 
	'https://github.com/jqlang/jq/commit/16170910332b51f1ff497ef566d6a525acdb5b43',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/16170910332b51f1ff497ef566d6a52
	5acdb5b43/comments',
			'author': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': 'd14393f5522531f57b8e3a83c04b7990c64a249e',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/d14393f5522531f57b8e3a83c04b799
	0c64a249e',
					'html_url': 
	'https://github.com/jqlang/jq/commit/d14393f5522531f57b8e3a83c04b7990c64a249e'
				}
			]
		}
	]

</details>

We can use jq to extract just the first commit.

```ipython
>>> from jqpy import jq
>>> jq(r'.[0]', data)
```

<details>
  	<summary>Show result</summary>

	[
		{
			'sha': 'bfb7fd570f521ef832fe1c3bca0e05abd398284c',
			'node_id': 
	'C_kwDOAE3WVdoAKGJmYjdmZDU3MGY1MjFlZjgzMmZlMWMzYmNhMGUwNWFiZDM5ODI4NGM',
			'commit': {
				'author': {
					'name': 'David Korczynski',
					'email': 'david@adalogics.com',
					'date': '2023-11-30T13:33:01Z'
				},
				'committer': {
					'name': 'Emanuele Torre',
					'email': 'torreemanuele6@gmail.com',
					'date': '2023-11-30T13:40:36Z'
				},
				'message': 'jq_fuzz_execute: cleanup un-needed 
	extern\n\nSigned-off-by: David Korczynski <david@adalogics.com>',
				'tree': {
					'sha': '47b08e6bc3e47c9ab13092d613bda7e4cf35bba0',
					'url': 
	'https://api.github.com/repos/jqlang/jq/git/trees/47b08e6bc3e47c9ab13092d613bda
	7e4cf35bba0'
				},
				'url': 
	'https://api.github.com/repos/jqlang/jq/git/commits/bfb7fd570f521ef832fe1c3bca0
	e05abd398284c',
				'comment_count': 0,
				'verification': {
					'verified': False,
					'reason': 'unsigned',
					'signature': None,
					'payload': None
				}
			},
			'url': 
	'https://api.github.com/repos/jqlang/jq/commits/bfb7fd570f521ef832fe1c3bca0e05a
	bd398284c',
			'html_url': 
	'https://github.com/jqlang/jq/commit/bfb7fd570f521ef832fe1c3bca0e05abd398284c',
			'comments_url': 
	'https://api.github.com/repos/jqlang/jq/commits/bfb7fd570f521ef832fe1c3bca0e05a
	bd398284c/comments',
			'author': {
				'login': 'DavidKorczynski',
				'id': 657617,
				'node_id': 'MDQ6VXNlcjY1NzYxNw==',
				'avatar_url': 'https://avatars.githubusercontent.com/u/657617?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/DavidKorczynski',
				'html_url': 'https://github.com/DavidKorczynski',
				'followers_url': 
	'https://api.github.com/users/DavidKorczynski/followers',
				'following_url': 
	'https://api.github.com/users/DavidKorczynski/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/DavidKorczynski/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/DavidKorczynski/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/DavidKorczynski/subscriptions',
				'organizations_url': 
	'https://api.github.com/users/DavidKorczynski/orgs',
				'repos_url': 'https://api.github.com/users/DavidKorczynski/repos',
				'events_url': 
	'https://api.github.com/users/DavidKorczynski/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/DavidKorczynski/received_events',
				'type': 'User',
				'site_admin': False
			},
			'committer': {
				'login': 'emanuele6',
				'id': 20175435,
				'node_id': 'MDQ6VXNlcjIwMTc1NDM1',
				'avatar_url': 
	'https://avatars.githubusercontent.com/u/20175435?v=4',
				'gravatar_id': '',
				'url': 'https://api.github.com/users/emanuele6',
				'html_url': 'https://github.com/emanuele6',
				'followers_url': 
	'https://api.github.com/users/emanuele6/followers',
				'following_url': 
	'https://api.github.com/users/emanuele6/following{/other_user}',
				'gists_url': 
	'https://api.github.com/users/emanuele6/gists{/gist_id}',
				'starred_url': 
	'https://api.github.com/users/emanuele6/starred{/owner}{/repo}',
				'subscriptions_url': 
	'https://api.github.com/users/emanuele6/subscriptions',
				'organizations_url': 'https://api.github.com/users/emanuele6/orgs',
				'repos_url': 'https://api.github.com/users/emanuele6/repos',
				'events_url': 
	'https://api.github.com/users/emanuele6/events{/privacy}',
				'received_events_url': 
	'https://api.github.com/users/emanuele6/received_events',
				'type': 'User',
				'site_admin': False
			},
			'parents': [
				{
					'sha': '252ab244cead3670a11d06bc3110f3a4577a2341',
					'url': 
	'https://api.github.com/repos/jqlang/jq/commits/252ab244cead3670a11d06bc3110f3a
	4577a2341',
					'html_url': 
	'https://github.com/jqlang/jq/commit/252ab244cead3670a11d06bc3110f3a4577a2341'
				}
			]
		}
	]

</details>

Here we invoke `jq` function to process JSON compatible `data` with `r'.[0]'` filtration expression. Function `jq` always returns list of JSON compatible results. In the most cases there will be only one result.

> [!NOTE]  
> Raw-string literal (prefixed with *r* symbol) is not necessary here but be careful about mixing pythonic escape sequences with jq formatting expression.

There's a lot of info we don't care about there, so we'll restrict it down to the most interesting fields.

```ipython
>>> jq(r'.[0] | {message: .commit.message, name: .commit.committer.name}', data)
```

<details>
  	<summary>Show result</summary>

	[
		{
			'message': 'jq_fuzz_execute: cleanup un-needed extern\n\nSigned-off-by:
	David Korczynski <david@adalogics.com>',
			'name': 'Emanuele Torre'
		}
	]

</details>

The `|` operator in jq feeds the output of one filter (`.[0]` which gets the first element of the array in the response) into the input of another (`{...}` which builds an object out of those fields). You can access nested attributes, such as `.commit.message`.

Now let's get the rest of the commits.

```ipython
>>> jq(r'.[] | {message: .commit.message, name: .commit.committer.name}', data)
```

<details>
  	<summary>Show result</summary>

	[
		{
			'message': 'jq_fuzz_execute: cleanup un-needed extern\n\nSigned-off-by:
	David Korczynski <david@adalogics.com>',
			'name': 'Emanuele Torre'
		},
		{
			'message': 'Add fuzzer targeting jq_next\n\nSigned-off-by: David 
	Korczynski <david@adalogics.com>',
			'name': 'Emanuele Torre'
		},
		{
			'message': 'jq_fuzz_compile: dump disassembly\n\nSigned-off-by: David 
	Korczynski <david@adalogics.com>',
			'name': 'Emanuele Torre'
		},
		{
			'message': 'Convert decnum to binary64 (double) instead of 
	decimal64\n\nThis is what the JSON spec suggests and will also be less 
	confusing compared to other jq implementations and langauges.\r\n\r\nRelated to
	#2939',
			'name': 'GitHub'
		},
		{
			'message': 'website: use https URLs instead of http URLs in download 
	page\n\nAlso add markdown formatting for decNumber URL so it gets rendered as 
	a\nlink in the html page.',
			'name': 'Emanuele Torre'
		}
	]

</details>

`.[]` returns each element of the array returned in the response, one at a time, which are all fed into `{message: .commit.message, name: .commit.committer.name}`.

If you want to get the output as a single array, you can tell jq to "collect" all the answers by wrapping the filter in square brackets:

```ipython
>>> jq(r'[.[] | {message: .commit.message, name: .commit.committer.name}]', data)
```

<details>
  	<summary>Show result</summary>

	[
		[
			{
				'message': 'jq_fuzz_execute: cleanup un-needed 
	extern\n\nSigned-off-by: David Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre'
			},
			{
				'message': 'Add fuzzer targeting jq_next\n\nSigned-off-by: David 
	Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre'
			},
			{
				'message': 'jq_fuzz_compile: dump disassembly\n\nSigned-off-by: 
	David Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre'
			},
			{
				'message': 'Convert decnum to binary64 (double) instead of 
	decimal64\n\nThis is what the JSON spec suggests and will also be less 
	confusing compared to other jq implementations and langauges.\r\n\r\nRelated to
	#2939',
				'name': 'GitHub'
			},
			{
				'message': 'website: use https URLs instead of http URLs in 
	download page\n\nAlso add markdown formatting for decNumber URL so it gets 
	rendered as a\nlink in the html page.',
				'name': 'Emanuele Torre'
			}
		]
	]

</details>

Next, let's try getting the URLs of the parent commits out of the API results as well. In each commit, the GitHub API includes information about "parent" commits. There can be one or many.

	"parents": [
	  {
		"sha": "f2ad9517c72f6267ae317639ab56bbfd4a8653d4",
		"url": "https://api.github.com/repos/jqlang/jq/commits/f2ad9517c72f6267ae317639ab56bbfd4a8653d4",
		"html_url": "https://github.com/jqlang/jq/commit/f2ad9517c72f6267ae317639ab56bbfd4a8653d4"
	  }
	]

We want to pull out all the "html_url" fields inside that array of parent commits and make a simple list of strings to go along with the "message" and "author" fields we already have.

```ipython
>>> jq(r'[.[] | {message: .commit.message, name: .commit.committer.name, parents: [.parents[].html_url]}]', data)
```

<details>
  	<summary>Show result</summary>

	[
		[
			{
				'message': 'jq_fuzz_execute: cleanup un-needed 
	extern\n\nSigned-off-by: David Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre',
				'parents': [
					'https://github.com/jqlang/jq/commit/252ab244cead3670a11d06bc31
	10f3a4577a2341'
				]
			},
			{
				'message': 'Add fuzzer targeting jq_next\n\nSigned-off-by: David 
	Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre',
				'parents': [
					'https://github.com/jqlang/jq/commit/13353515bd3aedf84c6e6ebfb7
	26563ae84db778'
				]
			},
			{
				'message': 'jq_fuzz_compile: dump disassembly\n\nSigned-off-by: 
	David Korczynski <david@adalogics.com>',
				'name': 'Emanuele Torre',
				'parents': [
					'https://github.com/jqlang/jq/commit/98a206964d59143c6ed9189b91
	cdb34af1ae5071'
				]
			},
			{
				'message': 'Convert decnum to binary64 (double) instead of 
	decimal64\n\nThis is what the JSON spec suggests and will also be less 
	confusing compared to other jq implementations and langauges.\r\n\r\nRelated to
	#2939',
				'name': 'GitHub',
				'parents': [
					'https://github.com/jqlang/jq/commit/16170910332b51f1ff497ef566
	d6a525acdb5b43'
				]
			},
			{
				'message': 'website: use https URLs instead of http URLs in 
	download page\n\nAlso add markdown formatting for decNumber URL so it gets 
	rendered as a\nlink in the html page.',
				'name': 'Emanuele Torre',
				'parents': [
					'https://github.com/jqlang/jq/commit/d14393f5522531f57b8e3a83c0
	4b7990c64a249e'
				]
			}
		]
	]

</details>

Here we're making an object as before, but this time the parents field is being set to `[.parents[].html_url]`, which collects all the parent commit URLs defined in the parents object.



> [!NOTE]  
> Visit original tutorial [website](https://jqlang.github.io/jq/manual/) to see more examples and read about JQ filtration language.

# Installation

1. Install JQ binary for your platform and include it to `PATH` environment variable (should be included by default).

   [JQ download page](https://jqlang.github.io/jq/download/)

   Quick commands:

	* Windows + [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/): `winget install jqlang.jq`
	* Windows + [scoop](https://scoop.sh/): `scoop install jq`
	* Windows + [choco](https://chocolatey.org/): `choco install jq`
	* Windows + [exe](https://github.com/jqlang/jq/releases/download/jq-1.7/jq-windows-amd64.exe)
	* [Ubuntu](https://packages.ubuntu.com/jq): `sudo apt-get install jq`
	* [Arch](https://archlinux.org/packages/?q=jq): `sudo pacman -S jq`
	* macOS + [brew](https://brew.sh/): `brew install jq`

2. Install JQpy python binding via [pip](https://pip.pypa.io/en/stable/) or your favourite python package manager:

   `pip install jqpy`



