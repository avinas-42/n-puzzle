from bs4 import BeautifulSoup
import os
import webbrowser

def create_table(size, table):
    ret = ''
    bg = 'style="background-color: grey;"'
    for i in range(size):
        ret += '<tr style="height: 108px;">'
        for j in range(size):
            ret += f'''<td class="u-border-4 u-border-grey-dark-1 u-table-cell" {bg if table[i * size + j] == 0 else ''}><h1>{table[i * size + j]}</h1></td>'''
        ret += '</tr>'
    return ret

def create_group(size):
    ret = ''
    for i in range(size):
        ret += f'<col width="{100/size}%">'
    return ret

def create_div(elem, puzzle):
  nbstep = puzzle.nbstep + 1
  div = ''
  while elem.daddy != None:
    nbstep -= 1
    table = create_table(puzzle.size, elem.state.table)
    group = create_group(puzzle.size)
    dnone = 'class="dnone"'
    tmp = f'''
    <div id="step{nbstep}" {dnone if nbstep != 1 else ''}>
      <section class="u-align-center u-clearfix u-section-2" id="sec-2abe">
        <div class="u-align-left u-clearfix u-sheet u-sheet-1">
          <div class="u-expanded-width u-table u-table-responsive u-table-1">
            <table class="u-table-entity">
            <colgroup>{group}</colgroup>
            <tbody class="u-table-body">{table}</tbody>
            </table>
          </div>
        </div>
      </section>
      <a class="u-absolute-vcenter u-carousel-control u-carousel-control-prev u-grey-60 u-icon-circle u-spacing-9 u-carousel-control-1" href="#carousel-bd35" role="button" data-u-slide="prev"
        onclick="previous({nbstep})">
        <span aria-hidden="true">
          <svg viewBox="0 0 477.175 477.175"><path d="M145.188,238.575l215.5-215.5c5.3-5.3,5.3-13.8,0-19.1s-13.8-5.3-19.1,0l-225.1,225.1c-5.3,5.3-5.3,13.8,0,19.1l225.1,225
                    c2.6,2.6,6.1,4,9.5,4s6.9-1.3,9.5-4c5.3-5.3,5.3-13.8,0-19.1L145.188,238.575z"></path></svg>
        </span>
        <span class="sr-only">+Previous</span>
      </a>
      <a class="u-absolute-vcenter u-carousel-control u-carousel-control-next u-grey-60 u-icon-circle u-spacing-9 u-carousel-control-2" href="#carousel-bd35" role="button" data-u-slide="next"
        onclick="next({nbstep})">
        <span aria-hidden="true">
              <svg viewBox="0 0 477.175 477.175"><path d="M360.731,229.075l-225.1-225.1c-5.3-5.3-13.8-5.3-19.1,0s-5.3,13.8,0,19.1l215.5,215.5l-215.5,215.5
                    c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-4l225.1-225.1C365.931,242.875,365.931,234.275,360.731,229.075z"></path></svg>
        </span>
        <span class="sr-only">+Next</span>
      </a>
      <section class="u-align-center u-clearfix u-section-3" id="sec-31d6">
        <div class="u-clearfix u-sheet u-sheet-1">
          <div class="u-expanded-width u-list u-list-1">
            <div class="u-repeater u-repeater-1">
              <div class="u-align-center u-container-style u-list-item u-repeater-item">
                <div class="u-container-layout u-similar-container u-container-layout-1">
                  <h1 class="u-text u-title u-text-1" data-animation-name="counter" data-animation-event="scroll" data-animation-duration="3000">{nbstep}</h1>
                  <p class="u-text u-text-2">Step</p>
                </div>
              </div>
              <div class="u-align-center u-container-style u-list-item u-repeater-item">
                <div class="u-container-layout u-similar-container u-container-layout-2">
                  <h1 class="u-text u-title u-text-3" data-animation-name="counter" data-animation-event="scroll" data-animation-duration="3000">{puzzle.nbstep}</h1>
                  <p class="u-text u-text-4"> Number of step</p>
                </div>
              </div>
              <div class="u-align-center u-container-style u-list-item u-repeater-item">
                <div class="u-container-layout u-similar-container u-container-layout-3">
                  <h1 class="u-text u-title u-text-5" data-animation-name="counter" data-animation-event="scroll" data-animation-duration="3000">{puzzle.nbOpenSelected}</h1>
                  <p class="u-text u-text-6"> Complexity in time</p>
                </div>
              </div>
              <div class="u-align-center u-container-style u-list-item u-repeater-item">
                <div class="u-container-layout u-similar-container u-container-layout-4">
                  <h1 class="u-text u-title u-text-7" data-animation-name="counter" data-animation-event="scroll" data-animation-duration="3000">{puzzle.maxOpen}</h1>
                  <p class="u-text u-text-8"> Complexity in size</p>
                </div>
              </div>
            </div>
          </div>
      </section>
    </div>'''
    div += tmp
    elem = elem.daddy
  return div

        

def front(elem, puzzle):
  div = create_div(elem, puzzle)
  script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
  rel_path = "NPUZZLE.html"
  abs_file_path = os.path.join(script_dir, rel_path)
  tmp = ''
  save = ['', '||||', '']
  with open(abs_file_path) as fp:
    data = fp.read()
    tab = data.split('||')
    save[0] = tab[0]
    save[2] = tab[2]
    tmp1 = data.split('||')
    tmp1[1] = div
    tmp = ''.join(tmp1)
  
  with open(abs_file_path, "w") as fp:
    fp.write(tmp)

  webbrowser.open('file://' + abs_file_path,new=2)

  with open(abs_file_path, "w") as fp:
    fp.write(''.join(save))