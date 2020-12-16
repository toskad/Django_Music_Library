<h1 align="center"> Django Music Library</h1>
  <h2>Popis Projektu</h2>
    <ul>
      <li>
        Toto je repozitář pro závěrečný projekt k maturitě.
      </li>
      <li>
        Projekt má sloužit jako webová aplikaci pro přehrávání hudby z databáze.
      </li>
      <li>
        Aplikace je vytvořena za pomoci Djanga a všechny data se ukládají do databáze SQlite3.
      </li>
    </ul>
  <h2>Využité technologie</h2>
    <li>
      Celá aplikace je tvořena v Djangu
    </li>
    <li>
      Pro databázi využívám SQlite3
    </li>
    <li>
      Zobrazované šablony jsou psané v HTML
    </li>
    <li>
      Lepší vzhled a responzivitu zajišťuje Bootstrap4
    </li>
  <h2>Cíle Projektu</h2>
    <p>
      &#10004; - Hotovo, &#9997; - Rozpracováno, &#10006; - Nevyhotoveno.
    </p>
    <ul>
      <li>
        Přehrávání hudby. &#10004;
      </li>
      <li>
        Rozdělení hudby podle žánru, autora a alb. &#10004;
      </li>
      <li>
        Možnost registrace uživatelů. &#10004;
      </li>
      <li>
        Přidávání hudby, alb a playlistů do oblíbených. &#10004;
      </li>
      <li>
        Vytváření playlistů. &#10004;
      </li>
      <li>
        Lepší zabezpečení url. &#10004;
      </li>
      <li>
        Lepší vzhled a responzivita. &#9997;
      </li>
      <li>
        Přehrávání hudby nejen na určité stránce. &#10006;
      </li>
    </ul>
  <h2>Spuštění Projektu</h2>
  <h4>Windows</h4>
    
    git clone https://github.com/it1726/Django_Music_Library
    cd Django_Music_Library
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py runserver
    
  <h4>Linux</h4>
  
    git clone https://github.com/it1726/Django_Music_Library
    cd Django_Music_Library
    virtualenv -p python venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver



