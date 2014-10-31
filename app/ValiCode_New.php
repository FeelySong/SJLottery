<?php 
$config = ['font_size'   => 15,
    'img_height'  => 28,
    'word_type'  => 1,
    'img_width'   => 105,
    'use_boder'   => TRUE,
    'font_file'   => 'arial.ttf',
    'wordlist_file'   => 'words.txt',
    'filter_type' => 5];
$sessSavePath = "sessions/";

if (!echo_validate_image($config))
{
    @session_start();
    $_SESSION['valicode'] = strtolower('3825');
    $im = @imagecreatefromjpeg('vdcode.jpg');
    header("Pragma:no-cache\r\n");
    header("Cache-Control:no-cache\r\n");
    header("Expires:0\r\n");
    imagejpeg($im);
    imagedestroy($im);
}

function echo_validate_image( $config = array() )
{
    @session_start();

    $font_size   = isset($config['font_size']) ? $config['font_size'] : 14;
    $img_height  = isset($config['img_height']) ? $config['img_height'] : 24;
    $img_width   = isset($config['img_width']) ? $config['img_width'] : 68;
    $font_file   = isset($config['font_file']) ? $config['font_file'] : PATH_DATA.'ggbi.ttf';
    $use_boder   = isset($config['use_boder']) ? $config['use_boder'] : TRUE;
    $filter_type = isset($config['filter_type']) ? $config['filter_type'] : 0;

    $im = @imagecreate($img_width, $img_height);
    imagecolorallocate($im, 255,255,255);

    $fontColor  = imagecolorallocate($im, 0x15, 0x15, 0x15);
//    $fontColor[]  = imagecolorallocate($im, 0x95, 0x1e, 0x04);
//   $fontColor[]  = imagecolorallocate($im, 0x93, 0x14, 0xa9);
//    $fontColor[]  = imagecolorallocate($im, 0x12, 0x81, 0x0a);
//    $fontColor[]  = imagecolorallocate($im, 0x06, 0x3a, 0xd5);

    $rndstring  = '';

        for($i=0; $i<4; $i++)
        {
            if ($config['word_type'] == 1)
            {
                $c = chr(mt_rand(48, 57));
            } else if($config['word_type'] == 2)
            {
                $c = chr(mt_rand(65, 90));
                if( $c=='I' ) $c = 'P';
                if( $c=='O' ) $c = 'N';
            }
            $rndstring .= $c;
        }

    $_SESSION['valicode'] = strtolower($rndstring);

    $rndcodelen = strlen($rndstring);
        for($i=0;$i<200;$i++){
                $randcolor = ImageColorallocate($im,rand(0,255),rand(0,255),rand(0,255));
                imagesetpixel($im, rand()%100, rand()%30, $randcolor);
        }

    if( $use_boder && $filter_type == 0 )
    {
        $bordercolor = imagecolorallocate($im, 0x9d, 0x9e, 0x96);
        imagerectangle($im, 0, 0, $img_width-1, $img_height-1, $bordercolor);
    }

    $lastc = '';
    for($i=0;$i<$rndcodelen;$i++)
    {
        $bc = mt_rand(0, 1);
        $rndstring[$i] = strtoupper($rndstring[$i]);
        $c_fontColor = $fontColor;
        $y_pos = $i==0 ? 12 : $i*($font_size+2)+12;
        $c = mt_rand(0, 15);
        @imagettftext($im, $font_size, 0, $y_pos, 23, $c_fontColor, $font_file, $rndstring[$i]);
        $lastc = $rndstring[$i];
    }

    switch($filter_type)
    {
        case 1:
            imagefilter ( $im, IMG_FILTER_NEGATE);
            break;
        case 2:
            imagefilter ( $im, IMG_FILTER_EMBOSS);
            break;
        case 3:
            imagefilter ( $im, IMG_FILTER_EDGEDETECT);
            break;
        default:
            break;
    }

    header("Pragma:no-cache\r\n");
    header("Cache-Control:no-cache\r\n");
    header("Expires:0\r\n");


    if(function_exists("imagejpeg"))
    {
        header("content-type:image/jpeg\r\n");
        imagejpeg($im);
    }
    else
    {
        header("content-type:image/png\r\n");
        imagepng($im);
    }
    imagedestroy($im);
    exit();
}