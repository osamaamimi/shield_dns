def parse(data: bytes) -> str:

    if len(data) < 13 :
        raise ValueError("packet too short") # error

    index = 12
    labels = []

    while True:
        if index >= len(data) :
            raise ValueError("invalid index length")

        length = data[index]
        if length == 0:
            break

        if length > 63 :
            raise ValueError("invalid label length")

        index += 1

        if (index + length) > len(data) :
            raise ValueError("label exceeds packet")

        label = data[index:index + length].decode("ascii")
        labels.append(label)
        index += length

    domain = ".".join(labels)

    return domain

