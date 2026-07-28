def main() -> None:
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS RAISE AN UNCAUGHT EXCEPTION"
    )

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(f"{dark_spell_record('Darkness', 'Bats and frogs')}")


if __name__ == "__main__":
    main()
