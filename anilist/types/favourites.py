#!/usr/bin/env python3
# Copyright (C) 2021-2022 Amano Team <https://amanoteam.com/>
#
# SPDX-License-Identifier: MIT

from typing import Callable, Dict, List

from .anime import Anime
from .character import Character
from .manga import Manga
from .staff import Staff, Studio


class FavouritesUnion:
    """Favourites union containing all
    anime, manga, character, staff and studio
    favourites of a user."""

    def __init__(
        self,
        *,
        anime: List[Anime] = [],
        manga: List[Manga] = [],
        characters: List[Character] = [],
        staff: List[Staff] = [],
        studios: List[Studio] = [],
    ) -> None:
        self.anime = anime
        self.manga = manga
        self.characters = characters
        self.staff = staff
        self.studios = studios

    def raw(self) -> Dict:
        return self.__dict__

    def __repr__(self) -> Callable:
        return self.__str__()

    def __str__(self) -> str:
        return str(self.raw())
