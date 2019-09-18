============================
为Foobar2000添加MIDI播放支持
============================

下载MIDI解码器：
----------------

http://www.foobar2000.org/components/view/foo_midi

下载并打开名为 :guilabel:`foo_midi.fb2k-component` 的文件，该插件自动添加到组件库后点击Apply并重启播放器。

安装音效库文件
--------------

默认的MIDI音色非常难听。以钢琴音色Yamaha S-YXG50为例，切换音色库的方法如下：

1. 在Foobar2000的安装目录下，新建名为 :guilabel:`vsti` 的文件夹，将 **音效库文件** 放进去。

2. Foobar2000依次展开 Preferences → Advanced → Playback → MIDI Decoder → VSTi search patch ，填入 :guilabel:`vsti` 目录的绝对路径。

3. 展开 ``Preferences → Playback → Input → MIDI Player`` ，选择Output一栏中的Plug-in，在下拉菜单中选择Yamaha S-YXG50即可。

附该音色库作者链接 http://veg.by/en/projects/syxg50