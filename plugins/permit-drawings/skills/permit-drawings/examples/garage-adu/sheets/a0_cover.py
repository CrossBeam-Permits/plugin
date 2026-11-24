"""A-0 - COVER SHEET."""

def build(kit):
    p = kit.project
    sh = kit.sheet("A-0")
    t = sh.panel((0, 18.4, 26.4, 4.0))
    t.banner(p.meta["title"], [p.meta["address"], "ACCESSORY DWELLING UNIT - CONVERSION OF AN (E) DETACHED GARAGE"])
    a = sh.panel((0, 8.4, 13.0, 9.6), "PROJECT DATA")
    a.table([("ITEM", 2.8), ("VALUE", None, "wrap")], size=9.5, rows=[
        ["PROPERTY OWNER", p.meta["owner"]], ["ADDRESS", p.meta["address"]],
        ["SCOPE", "CONVERT AN (E) DETACHED ONE-CAR GARAGE TO A ONE-BEDROOM ACCESSORY DWELLING UNIT."],
        ["FLOOR AREA", kit.text("{floor_area:sf}")],
        ["CODE BASIS", "PENDING: FROM CROSSBEAM CODE DATA FOR THIS JURISDICTION"],
    ])
    b = sh.panel((13.4, 8.4, 13.0, 9.6), "SHEET INDEX")
    sh.sheet_index(b, size=10)
    c = sh.panel((0, 0, 13.0, 8.0), "SCOPE OF WORK")
    c.numbered(["REMOVE (E) GARAGE DOOR AND TRACK. INFILL THE OPENING WITH A NEW 2x4 WALL, ENTRY DOOR D-1 AND WINDOW W-1.",
                "NEW BATH, KITCHENETTE, BEDROOM AND CLOSET PARTITIONS.", "NEW ELECTRICAL SUBPANEL."], size=9.5)
    return sh
