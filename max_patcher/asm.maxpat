{
	"patcher": {
		"fileversion": 1,
		"appversion": {
			"major": 8,
			"minor": 6,
			"revision": 5,
			"architecture": "x64",
			"modernui": 1
		},
		"classnamespace": "box",
		"rect": [
			836.0,
			305.0,
			1091.0,
			887.0
		],
		"bglocked": 0,
		"openinpresentation": 0,
		"default_fontsize": 12.0,
		"default_fontface": 0,
		"default_fontname": "Arial",
		"gridonopen": 1,
		"gridsize": [
			15.0,
			15.0
		],
		"gridsnaponopen": 1,
		"objectsnaponopen": 1,
		"statusbarvisible": 2,
		"toolbarvisible": 1,
		"lefttoolbarpinned": 0,
		"toptoolbarpinned": 0,
		"righttoolbarpinned": 0,
		"bottomtoolbarpinned": 0,
		"toolbars_unpinned_last_save": 0,
		"tallnewobj": 0,
		"boxanimatetime": 200,
		"enablehscroll": 1,
		"enablevscroll": 1,
		"devicewidth": 0.0,
		"description": "",
		"digest": "",
		"tags": "",
		"style": "",
		"subpatcher_template": "",
		"assistshowspatchername": 0,
		"boxes": [
			{
				"box": {
					"id": "obj-5",
					"maxclass": "newobj",
					"numinlets": 1,
					"numoutlets": 0,
					"patching_rect": [
						375.0,
						493.0,
						66.0,
						22.0
					],
					"text": "asm.return"
				}
			},
			{
				"box": {
					"id": "obj-3",
					"maxclass": "newobj",
					"numinlets": 2,
					"numoutlets": 1,
					"outlettype": [
						"signal"
					],
					"patching_rect": [
						375.0,
						411.0,
						74.0,
						22.0
					],
					"text": "asm.mul 0.1"
				}
			},
			{
				"box": {
					"id": "obj-2",
					"maxclass": "newobj",
					"numinlets": 1,
					"numoutlets": 1,
					"outlettype": [
						"signal"
					],
					"patching_rect": [
						379.0,
						326.0,
						75.0,
						22.0
					],
					"text": "asm.sin_osc"
				}
			},
			{
				"box": {
					"id": "obj-1",
					"maxclass": "newobj",
					"numinlets": 1,
					"numoutlets": 1,
					"outlettype": [
						"signal"
					],
					"patching_rect": [
						379.0,
						277.0,
						81.0,
						22.0
					],
					"text": "asm.mov 333"
				}
			}
		],
		"lines": [
			{
				"patchline": {
					"destination": [
						"obj-2",
						0
					],
					"source": [
						"obj-1",
						0
					]
				}
			},
			{
				"patchline": {
					"destination": [
						"obj-3",
						0
					],
					"source": [
						"obj-2",
						0
					]
				}
			},
			{
				"patchline": {
					"destination": [
						"obj-5",
						0
					],
					"source": [
						"obj-3",
						0
					]
				}
			}
		],
		"dependency_cache": [
			{
				"name": "asm.mov.maxpat",
				"bootpath": "~/dev/PyDotON/max_patcher/dependables",
				"patcherrelativepath": "./dependables",
				"type": "JSON",
				"implicit": 1
			},
			{
				"name": "asm.mul.maxpat",
				"bootpath": "~/dev/PyDotON/max_patcher/dependables",
				"patcherrelativepath": "./dependables",
				"type": "JSON",
				"implicit": 1
			},
			{
				"name": "asm.return.maxpat",
				"bootpath": "~/dev/PyDotON/max_patcher/dependables",
				"patcherrelativepath": "./dependables",
				"type": "JSON",
				"implicit": 1
			},
			{
				"name": "asm.sin_osc.maxpat",
				"bootpath": "~/dev/PyDotON/max_patcher/dependables",
				"patcherrelativepath": "./dependables",
				"type": "JSON",
				"implicit": 1
			}
		],
		"autosave": 0
	}
}