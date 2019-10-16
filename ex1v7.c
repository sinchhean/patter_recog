#include <stdio.h>
#include <stdlib.h> /* rand(), srand( )を使うための準備 */
#include <time.h>   /* time( )を使うための準備 */

#define ROW    4    /* マクロの定義 */
#define COLUMN 4    /*     同上     */

#define UP_KEY    65 /* マクロで↑キーの値を定義 */
#define DOWN_KEY  66 /* マクロで↓キーの値を定義 */
#define RIGHT_KEY 67 /* マクロで→キーの値を定義 */
#define LEFT_KEY  68 /* マクロで←キーの値を定義 */
#define SPACE ROW * COLUMN /* マクロで空白パネルの値を定義 */
#define UP 1        /* movePanel( )で使う定数の設定 */
#define DOWN 2      /*       同上                   */
#define RIGHT 3     /*       同上                   */
#define LEFT 4      /*       同上                   */

void initPuzzle();    /*  プロトタイプ宣言  */
void initScreen();    /*       同上         */
int scanInput();      /*       同上         */
void updatePuzzle();  /*       同上         */
int judge();          /*       同上         */
int movePanel( int ); /*       同上         */
void clearScreen();   /*       同上         */
void moveCursor();    /*       同上         */


/* 外部変数 */
int puzzle[ ROW ][ COLUMN ] = 
  {
    {  1,  2,  3,  4 },
    {  5,  6,  7,  8 },
    {  9, 10, 11, 12 },
    { 13, 14, 15, SPACE }
  };/* ２次元配列の宣言と代入（初期化） */


void main(){

  int direction;  /*  移動する方向を覚えておくための変数  */

  /* キーボードからの入力をすぐさま反映する呪文 */
  system( "stty -echo -icanon min 1 time 0" );

  /*  パズルの初期化  */
  initPuzzle();

  /*  画面の初期化  */
  initScreen();

  /*  無限ループで入力を何回でも受け付けるようにする  */
  while( 1 ){

    /*  パズルの表示を更新する  */
    updatePuzzle();

    /* 終了判定  */
    if( judge() ){
      break;
    }

    /*  カーソルキーからの入力（移動する方向）を受け取る  */
    direction = scanInput();

    /*  入力に応じてパズルを移動させる  */
    movePanel( direction );
    
  }

  /*  終了メッセージ  */
  printf("\n\n");
  printf("####################################################\n");
  printf("###############★☆★Clear!!!☆★☆#################\n");
  printf("####################################################\n\n\n");

  /* おまじないを解除！そうしないとこれ以降、文字が表示されなくなる */
  system( "stty echo -icanon min 1 time 0" );

}


/*  パズルの初期化を行う関数  */
/*  乱数を使って、パズルをばらばらな状態にする  */
void initPuzzle(){

  int i;

  for( i = 0; i < 1000; i++ ){
    movePanel(rand()%4 + 1);
  }
}


/*  画面の初期化を行う関数  */
/*  画面をクリアして、パズルのフレームを表示する  */
void initScreen(){
  
  clearScreen();

  printf("               15パズル  \n");
  printf("             ┏━━━┳━━━┳━━━┳━━━┓  \n");
  printf("             ┃   ┃   ┃   ┃   ┃  \n");
  printf("             ┣━━━╋━━━╋━━━╋━━━┫  \n");
  printf("             ┃   ┃   ┃   ┃   ┃  \n");
  printf("             ┣━━━╋━━━╋━━━╋━━━┫  \n");
  printf("             ┃   ┃   ┃   ┃   ┃  \n");
  printf("             ┣━━━╋━━━╋━━━╋━━━┫  \n");
  printf("             ┃   ┃   ┃   ┃   ┃  \n");
  printf("             ┗━━━┻━━━┻━━━┻━━━┛  \n");
  printf("      空白パネルの移動：← → ↑ ↓ キー\n");
}



/*  パズルの表示を更新する関数  */
/*  各パネルに数字や空白（■）を表示する  */
void updatePuzzle(){

  int i, j;

  for(i = 0; i < ROW ; i++){
    for(j = 0; j < COLUMN ; j++){
      moveCursor(j, i);
      if( puzzle[i][j] != SPACE ){
        printf("%2d", puzzle[i][j]);
      }
      else {
        printf("  ");
      }
    }
  }
    
  printf( "\x1b[13;1H" );

}


/*  入力処理をする関数  */
/*  やりたいことはこれまでの課題とおなじだが、ちょっと難しい  */
/*  くわしく知りたい人はＴＡに質問してください  */
int scanInput(){

  int ch;
  int flag = 1;
  int direction;

  /*  ← → ↑ ↓ キーを読むための特殊処理（ほかの入力は無視する）  */
  while( flag ){
    ch = getchar();
    if( flag == 1 && ch == 27 ){
      flag = 2;
    }
    if( flag == 2 && ch == 91 ){
      flag = 3;
    }
    if( flag == 3 && ( ch == 65 || ch == 66 || ch == 67 || ch == 68 ) ){
      flag = 0;
      direction = ch - 64;
    }
  }

  return direction;

}


/* パズルの終了判定をする関数  */
int judge(){

  int i, j;
  int counter = 1; /* パズルが合っているかの確認用カウンタ変数 */
  
  /* パズルの左上から順番にカウントアップしていき */
  /* 配列の中身と完成形と一致してるかを判定。     */
  for( i = 0; i < ROW; i++ ){
    for( j = 0; j < COLUMN; j++ ){
      if( puzzle[ i ][ j ] != counter++ ){
	return 0;
      }
    }
  }

  return 1;

}


/*  指定された方向に空白パネルを移動させる関数  */
int movePanel( int direction ){

  int i,j;
  int flag = 1;
  int x, y;
  int spaceX, spaceY;

  /* 移動するパネルとスペースの座標を求める */
  for( i=0; i < ROW; i++ ){
    for( j=0; j < COLUMN; j++ ){
      if( puzzle[ i ][ j ] == SPACE ){
	spaceX = j;
	spaceY = i;
      }
    }
  }

  /* 移動先の座標を求める */
  x = spaceX;
  y = spaceY;
  switch( direction ){
  case UP:
    if( y == 0 ){
      flag = 0;
    }
    y--;
    break;
  case DOWN:
    if( y == ROW - 1 ){
      flag = 0;
    }
    y++;
    break;
  case RIGHT:
    if( x == COLUMN - 1 ){
      flag = 0;
    }
    x++;
    break;
  case LEFT:
    if( x == 0 ){
      flag = 0;
    }
    x--;
    break;
  }


  /* 選択された方向に移動可能かどうかチェック */
  if( !flag ) { return 0; }

  /* 実際に移動 */
  /*
   * Y軸はROWに, X軸はCOLUMNに対応
   */
  puzzle[ spaceY ][ spaceX ] = puzzle[ y ][ x ];
  puzzle[ y ][ x ] = SPACE;

  /* おまじないを解除！そうしないとこれ以降、文字が表示されなくなる */
  system( "stty echo -icanon min 1 time 0" );

  return 1;

}


/* 画面をクリアする関数  */
void clearScreen(){

  printf( "\x1b[2J" );
  printf( "\x1b[1;1H" );
}


/*  端末（kterm）のカーソルを移動させる関数  */
void moveCursor( int x, int y ){
  int termX, termY;

  termX = 15 + ( x * 4 );
  termY = 3 + ( 2 * y );
  printf( "\x1b[%d;%dH", termY, termX );
}

