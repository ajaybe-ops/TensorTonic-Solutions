def deduplicate(records: list, key_columns: list, strategy: str) -> list:
    groups = {}

    for record in records:
        key = tuple(record[col] for col in key_columns)

        if key not in groups:
            groups[key] = []

        groups[key].append(record)

    result = []

    for key, items in groups.items():
        if strategy == "first":
            selected = items[0]

        elif strategy == "last":
            selected = items[-1]

        elif strategy == "most_complete":
            selected = items[0]

            for record in items[1:]:
                current_none = sum(v is None for v in selected.values())
                new_none = sum(v is None for v in record.values())

                if new_none < current_none:
                    selected = record

        result.append(selected)

    return result