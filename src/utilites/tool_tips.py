def create_toll_tip(sensor):
    type_s = ""
    state = ""

    match sensor["type"]:
        case 1:
            type_s = "ИП-535"
        case 2:
            type_s = "ИПП-Гелиос"
        case 3:
            type_s = "ИП-101"
        case 4:
            type_s = "ИП-330 Кречет"
        case 5:
            type_s = "ИП-329 Феникс"
        case 6:
            type_s = "ИПЭС"
        case 7:
            type_s = "МИП"
        case 8:
            type_s = "ИПА"
        case 9:
            type_s = "NLS16"
        case 10:
            type_s = "NLS8"
        case 51:
            type_s = "А2ДПИ"
        case 53:
            type_s = "АМК"
        case 54:
            type_s = "АР1"
        case 57:
            type_s = "АТИ"
        case 60:
            type_s = "ИР"
        case 65:
            type_s = "МКЗ"
        case 64:
            type_s = "ИСМ220-4"
        case 61:
            type_s = "ИСМ5"
        case 62:
            type_s = "ИСМ22"

    match sensor["state"]:
        case "N":
            state = "Норма"
        case "F":
            state = "Сработал"
        case "E":
            state = "Ошибка"

    if sensor["type"] > 50:
        out_str = """
            <p>Тип - <b>{type}</p> 
            <p>Адрес - <b>{slave}</p>
            <p>Серийный номер - <b>{sn}</p>
            <p>Состояние - <b>{state}</p> 
            """.format(
            type=type_s,
            state=state,
            slave=sensor["slave"],
            sn=sensor["serialnumber"]
        )
        return out_str
    else:
        out_str = """
            <p>Тип - <b>{type}</p> 
            <p>Адрес - <b>{slave}</p>
            <p>Состояние - <b>{state}</p> 
            """.format(
            type=type_s,
            state=state,
            slave=sensor["slave"],
        )
        return out_str
