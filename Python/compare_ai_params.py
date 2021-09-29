from soulstruct.darksouls1r.params import GameParamBND, Param


def main():
    vanilla_ai = GameParamBND(
        "F:/Steam/steamapps/common/DARK SOULS REMASTERED (Vanilla Backup)/param/GameParam/GameParam.parambnd.dcx"
    ).AI
    aggr_ai = Param("HyperAggression_NpcThinkParam.param")

    for i, entry in vanilla_ai.items():
        aggr = aggr_ai[i]
        print(i)
        for field_name, value in entry.fields.items():
            aggr_value = aggr[field_name]
            if value != aggr_value:
                print("  ", field_name, value, aggr_value)


if __name__ == '__main__':
    main()
