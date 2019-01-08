Babel Tower
===========

Python script to quickly edit Qt translations files.

Built for [mysthea-app](https://github.com/evonove/mysthea-app) but easily modifiable to be generic.

Usage
=====

    pipenv install
    pipenv shell
    python babel-tower.py input.csv app_de.ts ENG GER

Given an `input.csv`:

    ENG;GER;ITA;JAP
    River;Fluss;Fiume;河
    Mountain;Gebirge;Montagna;山
    Forest;Wald;Foresta;森
    Land of Myst;Nebelland;Terra Nebbiosa;ミストランド
    Crystal Field;Kristallfeld;Campo di Cristallo;クリスタルフィールド
    Storm;Sturm;Tempesta ;ストーム

and Qt translation file `app_de.ts`:


    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE TS>
    <TS version="2.1" language="de_DE">
    <context>
        <name>CardsData</name>
        <message>
            <source>River</source>
            <translation type="unfinished"></translation>
        </message>
        <message>
            <source>Mountain</source>
            <translation type="unfinished"></translation>
        </message>
        <message>
            <source>Forest</source>
            <translation type="unfinished"></translation>
        </message>
        <message>
            <source>Land of Myst</source>
            <translation type="unfinished"></translation>
        </message>
        <message>
            <source>Crystal Field</source>
            <translation type="unfinished"></translation>
        </message>
        <message>
            <source>Storm</source>
            <translation type="unfinished"></translation>
        </message>
    </context>
    </TS>

The result of the previous command would be this:

    <?xml version="1.0" encoding="utf-8"?>
    <!DOCTYPE TS>
    <TS version="2.1" language="de_DE">
    <context>
        <name>CardsData</name>
        <message>
            <source>River</source>
            <translation>Fluss</translation>
        </message>
        <message>
            <source>Mountain</source>
            <translation>Gebirge</translation>
        </message>
        <message>
            <source>Forest</source>
            <translation>Wald</translation>
        </message>
        <message>
            <source>Land of Myst</source>
            <translation>Nebelland</translation>
        </message>
        <message>
            <source>Crystal Field</source>
            <translation>Kristallfeld</translation>
        </message>
        <message>
            <source>Storm</source>
            <translation>Sturm</translation>
        </message>
    </context>
    </TS>


Code formatting
===============

It's a little script but a tidy one nonetheless so, please, use [black](https://github.com/ambv/black) with this arguments:

    --line-length 120 --py36 --skip-numeric-underscore-normalization
